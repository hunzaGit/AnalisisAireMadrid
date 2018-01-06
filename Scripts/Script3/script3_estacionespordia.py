from __future__ import print_function
from pyspark import SparkConf, SparkContext

#El script da como resultado, por cada linea, las cantidades de NO2 (en cada una de las 24 estaciones) 
#en cada día anyo que tuviese datos registrados y validos

conf = SparkConf().setMaster('local').setAppName('CantidadDiariaPorEstacion')
sc = SparkContext(conf = conf)

#Lectura del fichero 
rdd = sc.textFile("datos201711.txt")

#Separa usando la coma como patron
lineas = rdd.map(lambda line: line.split(","))

#Selecciona todas las lineas cuyo cuarto valor sea 08, las que tienen medidas del NO2
lineas_no2 = lineas.filter(lambda valor: valor[3]=='08')

#Funcion que da formato a la fecha, por cada linea nos devuelve mes/dia/anyo, codigo_estacion y cantidad_no2
def formatearDias(linea):
	array = []
	estacion = linea[0]+linea[1]+linea[2]
	anyo = linea[6]
	mes = linea[7]
	dia = 1
	diaStr = ''
	for i in range(9, len(linea), 2):
		if linea[i] == 'V':
			if dia >= 1 and dia <= 9:
				diaStr = '0' + str(dia)
			else:
				diaStr = str(dia)
			array.append(( mes + '/' + diaStr + '/' + anyo, float(linea[i - 1])))
			dia += 1
		else:
			dia += 1
	return array
#------------------------------------Fin funcion------------------------------------------
resultados_formateados = lineas_no2.flatMap(formatearDias)

lineas = resultados_formateados.groupByKey().map(lambda x : (x[0],list(x[1])))
lineas = lineas.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))

lineas.saveAsTextFile("output.csv")

#OUTPUT: mes/dia/anyo;cant_no2_estacionX;cant_no2_estacionY;...;cant_no2_estacionN
# 01/01/2017;50;53;...
# 01/02/2017;62;64;...
# ...
