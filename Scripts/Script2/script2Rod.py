from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('MediaAnualPorDiasPorZona')
sc = SparkContext(conf = conf)

zona1 = ['039','050','011','038','048','004','035','047','049','008']
zona2 = ['054','040','036']
zona3 = ['060','057','027','059','055','016']
zona4 = ['058','024']
zona5 = ['018','056','017']


#importamos el fichero 
rdd = sc.textFile("datos201711.txt")

#Divide por comas cada linea
lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(","))

#nos quedamos solo con los de codigo 08 que son los de no2
valor = lines.filter(lambda linea: linea[3]=='08')

#funcion que foamrtea los dias, por cada linea nos devuelve la estacio, la fecha y el valor
def formatearDias(line):
	array = []
	estacion = line[2]
	anyo = line[6]
	mes = line[7]
	dia = 1
	diaStr = ''
	for i in range(9, len(line), 2):
		if line[i] == 'V':
			if dia >= 1 and dia <= 9:
				diaStr = '0' + str(dia)
			else:
				diaStr = str(dia)
			array.append(( estacion, mes + '/' + diaStr + '/' + anyo, float(line[i - 1]))) # ( estacion, 'fecha', valorDia)
			dia += 1
		else:
			dia += 1
	return array
#------------------------------------Fin funcion------------------------------------------

#llamamos a la funcion que formatea los datos estacion, fecha,valor
valor = valor.flatMap(formatearDias)

listZonas= [[] for x in xrange(5)]

def disgregarZonas(line):
	global listZonas
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion in zona1:
		listZonas[0].append((fecha,valor))
	if estacion in zona2:
		listZonas[1].append((fecha,valor))
	if estacion in zona3:
		listZonas[2].append((fecha,valor))
	if estacion in zona4:
		listZonas[3].append((fecha,valor))
	if estacion in zona5:
		listZonas[4].append((fecha,valor))


valor.foreach(disgregarZonas)

print '**************************************************************************************************************************'
print listZonas
print '**************************************************************************************************************************'


unionZonas = sc.parallelize([])
for numZ in xrange(0,5):

	#llamamos a la funcion para que nos devuelva los datos del distrito 1	
	zona = sc.parallelize(listZonas[numZ])

	#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
	zonaAcum = zona.reduceByKey(lambda acum,n: acum+n)

	#con las siguientes dos lineas contamos el numero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
	numDias = zona.map(lambda tupla: (tupla[0],1))

	numDias = numDias.reduceByKey(lambda acum,n: acum+n)

	#juntamos el acumulado de no2 y el numero de veces de cada dia
	joinRDD = zonaAcum.join(numDias)
	# ('fecha', (totalDistrito, contDistrito))

	#calculamos la media
	mediaZona = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

	unionZonas = unionZonas.union(mediaZona)


unionZonas = unionZonas.groupByKey().map(lambda x : (x[0], list(x[1]) )).sortByKey()

unionZonasS = unionZonas.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
unionZonasS.saveAsTextFile("distritosRod.csv")
