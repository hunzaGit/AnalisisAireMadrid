from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('MediaAnualPorDias')
sc = SparkContext(conf = conf)

#importamos el fichero 
rdd = sc.textFile("datos201711.txt")

#Divide por comas cada linea
lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(","))

#nos quedamos solo con los de codigo 08 que son los de no2
valor = lines.filter(lambda valor: valor[3]=='08')

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
			array.append(( estacion, mes + '/' + diaStr + '/' + anyo, float(line[i - 1])))
			dia += 1
		else:
			dia += 1
	return array
#------------------------------------Fin funcion------------------------------------------

#llamamos a la funcion que formatea los datos estacion, fecha,valor
valor = valor.flatMap(formatearDias)

#funcion que filtra y nos devuelve los datos de las estaciones del distrito o zona 1
#ya no devolvemos la estacion por que lo que devuelva la funcion se lo asignaremos al distrito 1
def distrito1(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '038' or estacion == '048' or estacion == '004' or estacion == '035':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------
	
#llamamos a la funcion para que nos devuelva los datos del distrito 1	
distrit1 = valor.flatMap(distrito1)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit1Acum = distrit1.reduceByKey(lambda acum,n: acum+n)

#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit1.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit1Acum.join(numDias)

#calculamos la media
mediaAnualdistrito1 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito1 = mediaAnualdistrito1.sortByKey()

#funcion que filtra y nos devuelve los datos de las estaciones del distrito o zona 2
#ya no devolvemos la estacion por que lo que devuelva la funcion se lo asignaremos al distrito 2
def distrito2(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '050' or estacion == '011'or estacion == '039':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------	
	
#llamamos a la funcion para que nos devuelva los datos del distrito 2	
distrit2 = valor.flatMap(distrito2)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit2Acum = distrit2.reduceByKey(lambda acum,n: acum+n)

#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit2.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit2Acum.join(numDias)

#calculamos la media
mediaAnualdistrito2 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito2 = mediaAnualdistrito2.sortByKey()

#funcion que filtra y nos devuelve los datos de las estaciones del distrito o zona 3
#ya no devolvemos la estacion por que lo que devuelva la funcion se lo asignaremos al distrito 3
def distrito3(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '047' or estacion == '008'or estacion == '049' or estacion == '056':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------	
	
#llamamos a la funcion para que nos devuelva los datos del distrito 3
distrit3 = valor.flatMap(distrito3)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit3Acum = distrit3.reduceByKey(lambda acum,n: acum+n)

#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit3.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit3Acum.join(numDias)

#calculamos la media
mediaAnualdistrito3 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito3 = mediaAnualdistrito3.sortByKey()

#funcion que filtra y nos devuelve los datos de las estaciones del distrito o zona 4
#ya no devolvemos la estacion por que lo que devuelva la funcion se lo asignaremos al distrito 4
def distrito4(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '016' or estacion == '055' or estacion == '059' or estacion == '027' or estacion == '057':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------
	
#llamamos a la funcion para que nos devuelva los datos del distrito 4
distrit4 = valor.flatMap(distrito4)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit4Acum = distrit4.reduceByKey(lambda acum,n: acum+n)

#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit4.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit4Acum.join(numDias)

#calculamos la media
mediaAnualdistrito4 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito4 = mediaAnualdistrito4.sortByKey()

#funcion que filtra y nos devuelve los datos de las estaciones del distrito o zona 5
#ya no devolvemos la estacion por que lo que devuelva la funcion se lo asignaremos al distrito 5
def distrito5(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '054' or estacion == '040'or estacion == '036' or estacion == '017':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------	
	
#llamamos a la funcion para que nos devuelva los datos del distrito 5
distrit5 = valor.flatMap(distrito5)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit5Acum = distrit5.reduceByKey(lambda acum,n: acum+n)


#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit5.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit5Acum.join(numDias)

#calculamos la media
mediaAnualdistrito5 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito5 = mediaAnualdistrito5.sortByKey()


def distrito6(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '024' or estacion == '060'or estacion == '058' or estacion == '018':
		array.append((fecha,valor))
	return array
#---------------------------------Fin funcion---------------------------------------------	
	
#llamamos a la funcion para que nos devuelva los datos del distrito 5
distrit6 = valor.flatMap(distrito6)

#como los datos estan de la forma (fecha,valor) nos quedamos con (fecha,totalDistrito)
distrit6Acum = distrit6.reduceByKey(lambda acum,n: acum+n)


#con las siguientes dos lineas contamos el umero de veces que aparece cada dia obteniendo (fecha,3) donde 3 serian las veces
numDias = distrit6.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

#juntamos el acumulado de no2 y el numero de veces de cada dia
joinRDD = distrit6Acum.join(numDias)

#calculamos la media
mediaAnualdistrito6 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

#ordenamos por dia
mediaAnualdistrito6 = mediaAnualdistrito6.sortByKey()

#HASTA AQUI LO QUE TENEMOS ES LAS MEDIAS DE CADA DISTRITO DEL 1 AL 5 EN EL FORMATO (FECHA,VALOR) POR CADA DISTRITO

#Desde aqui
uniond1d2 = mediaAnualdistrito1.union(mediaAnualdistrito2)

uniond1d2d3 = uniond1d2.union(mediaAnualdistrito3)

uniond1d2d3d4 = uniond1d2d3.union(mediaAnualdistrito4)

uniond1d2d3d4d5 = uniond1d2d3d4.union(mediaAnualdistrito5)

uniond1d2d3d4d5d6 = uniond1d2d3d4d5.union(mediaAnualdistrito6)

uniond1d2d3d4d5d6 = uniond1d2d3d4d5d6.sortByKey()
#hasta aqui he unido todos los datos de cada distrito

#para luego aqui hacer el groupbykey y quedarme con una fecha y los 5 valores de los distritos
union = uniond1d2d3d4d5d6.groupByKey().map(lambda x : (x[0], list(x[1])))

#ordeno por fecha
union = union.sortByKey()

#convierto a formato csv
union = union.map(lambda tupla: tupla[0] + ';' + str(tupla[1][0]) + ';'+ str(tupla[1][1]) + ';'+ str(tupla[1][2])+ ';'+ str(tupla[1][3])+ ';'+ str(tupla[1][4]) +  ';'+ str(tupla[1][5]))


union.saveAsTextFile("distritos.csv")
