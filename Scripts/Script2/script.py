#from __future__ import print_function

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('MediaAnualPorDias')
sc = SparkContext(conf = conf)


rdd = sc.textFile("datos201711.txt")

lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(","))
#Divide por comas cada linea

#valor = lines.map(lambda valor: valor[0])
#coje un valor de cada linea

valor = lines.filter(lambda valor: valor[3]=='08')
#nos quedamos solo con los de codigo 08 que son los de no2

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
	
	
	
valor = valor.flatMap(formatearDias)
#estacion, fecha,valor

#valor.foreach(print)#para imprimir el valoor en pyspark


def distrito1(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '039' or estacion == '050'or estacion == '011' or estacion == '038' or estacion == '048' or estacion == '004' or estacion == '035' or estacion == '047' or estacion == '049' or estacion == '008':
		array.append((fecha,valor))
	return array

	
	
distrit1 = valor.flatMap(distrito1)

distrit1Acum = distrit1.reduceByKey(lambda acum,n: acum+n)

numDias = distrit1.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

joinRDD = distrit1Acum.join(numDias)

mediaAnualdistrito1 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

mediaAnualdistrito1 = mediaAnualdistrito1.sortByKey()

def distrito2(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '054' or estacion == '040'or estacion == '036':
		array.append((fecha,valor))
	return array
	
	
	
distrit2 = valor.flatMap(distrito2)

distrit2Acum = distrit2.reduceByKey(lambda acum,n: acum+n)

numDias = distrit2.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

joinRDD = distrit2Acum.join(numDias)

mediaAnualdistrito2 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

mediaAnualdistrito2 = mediaAnualdistrito2.sortByKey()

def distrito3(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '060' or estacion == '057'or estacion == '027' or estacion == '059' or estacion == '055' or estacion == '016':
		array.append((fecha,valor))
	return array
	
	
	
distrit3 = valor.flatMap(distrito3)

distrit3Acum = distrit3.reduceByKey(lambda acum,n: acum+n)

numDias = distrit3.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

joinRDD = distrit3Acum.join(numDias)

mediaAnualdistrito3 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

mediaAnualdistrito3 = mediaAnualdistrito3.sortByKey()

def distrito4(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '058' or estacion == '024':
		array.append((fecha,valor))
	return array
	
	
	
distrit4 = valor.flatMap(distrito4)

distrit4Acum = distrit4.reduceByKey(lambda acum,n: acum+n)

numDias = distrit4.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

joinRDD = distrit4Acum.join(numDias)

mediaAnualdistrito4 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

mediaAnualdistrito4 = mediaAnualdistrito4.sortByKey()

def distrito5(line):
	array=[]
	estacion = line[0]
	fecha = line[1]
	valor = line[2]
	if estacion == '018' or estacion == '056'or estacion == '017':
		array.append((fecha,valor))
	return array
	
	
	
distrit5 = valor.flatMap(distrito5)

distrit5Acum = distrit5.reduceByKey(lambda acum,n: acum+n)

numDias = distrit5.map(lambda tupla: (tupla[0],1))

numDias = numDias.reduceByKey(lambda acum,n: acum+n)

joinRDD = distrit5Acum.join(numDias)

mediaAnualdistrito5 = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2)))

mediaAnualdistrito5 = mediaAnualdistrito5.sortByKey()

uniond1d2 = mediaAnualdistrito1.union(mediaAnualdistrito2)

uniond1d2d3 = uniond1d2.union(mediaAnualdistrito3)

uniond1d2d3d4 = uniond1d2d3.union(mediaAnualdistrito4)

uniond1d2d3d4d5 = uniond1d2d3d4.union(mediaAnualdistrito5)

uniond1d2d3d4d5 = uniond1d2d3d4d5.sortByKey()

union = uniond1d2d3d4d5.groupByKey().map(lambda x : (x[0], list(x[1])))

union = union.sortByKey()

union = union.map(lambda tupla: tupla[0] + ';' + str(tupla[1][0]) + ';'+ str(tupla[1][1]) + ';'+ str(tupla[1][2])+ ';'+ str(tupla[1][3])+ ';'+ str(tupla[1][4]))


union.saveAsTextFile("distritos.csv")