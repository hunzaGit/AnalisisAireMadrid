from __future__ import print_function
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('CantidadDiariaPorEstacion')
sc = SparkContext(conf = conf)

#Lectura del fichero 
rdd = sc.textFile("datos201711.txt")

#Separa usando la coma como patron
lineas = rdd.map(lambda line: line.split(","))

#Selecciona todas las lineas cuyo cuarto valor sea 08, las que tienen medidas del NO2
lineas_no2 = lineas.filter(lambda valor: valor[3]=='08')

#funcion que foamrtea los dias, por cada linea nos devuelve la estacio, la fecha y el valor
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
			array.append(( mes + '/' + diaStr + '/' + anyo, estacion, float(linea[i - 1])))
			dia += 1
		else:
			dia += 1
	return array
#------------------------------------Fin funcion------------------------------------------
resultados_formateados = lineas_no2.flatMap(formatearDias)

def toCSVLine(data):
  return ';'.join(str(d) for d in data)

resultados_csv = resultados_formateados.map(toCSVLine)
resultados_csv.saveAsTextFile("output.csv")

#OUTPUT: mes/dia/anyo;estacionX;cant_no2_estacionX
# 01/01/2017;28079004;50
# 01/02/2017;28079004;62
# ...
