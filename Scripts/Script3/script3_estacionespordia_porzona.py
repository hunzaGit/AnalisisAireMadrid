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
	estacion = linea[2]
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
			array.append(( mes + '/' + diaStr + '/' + anyo, float(linea[i - 1]), estacion))
			dia += 1
		else:
			dia += 1
	return array
#------------------------------------Fin funcion------------------------------------------
resultados_formateados = lineas_no2.flatMap(formatearDias)

zona1 = ['039','050','011','038','048','004','035','047','049','008']
zona2 = ['054','040','036']
zona3 = ['060','057','027','059','055','016']
zona4 = ['058','024']
zona5 = ['018','056','017']

resultados_formateados_zona1 = resultados_formateados.filter(lambda valor: valor[2] in zona1)
resultados_formateados_zona2 = resultados_formateados.filter(lambda valor: valor[2] in zona2)
resultados_formateados_zona3 = resultados_formateados.filter(lambda valor: valor[2] in zona3)
resultados_formateados_zona4 = resultados_formateados.filter(lambda valor: valor[2] in zona4)
resultados_formateados_zona5 = resultados_formateados.filter(lambda valor: valor[2] in zona5)

resultados_formateados_zona1 = resultados_formateados_zona1.map(lambda valor: (valor[0], valor[1]))
resultados_formateados_zona2 = resultados_formateados_zona2.map(lambda valor: (valor[0], valor[1]))
resultados_formateados_zona3 = resultados_formateados_zona3.map(lambda valor: (valor[0], valor[1]))
resultados_formateados_zona4 = resultados_formateados_zona4.map(lambda valor: (valor[0], valor[1]))
resultados_formateados_zona5 = resultados_formateados_zona5.map(lambda valor: (valor[0], valor[1]))

#resultados_formateados.foreach(print)

resultados_formateados_zona1 = resultados_formateados_zona1.groupByKey().map(lambda x : (x[0],list(x[1])))
resultados_formateados_zona1 = resultados_formateados_zona1.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
resultados_formateados_zona1.saveAsTextFile("medicionesdiarias_zona1.csv")

resultados_formateados_zona2 = resultados_formateados_zona2.groupByKey().map(lambda x : (x[0],list(x[1])))
resultados_formateados_zona2 = resultados_formateados_zona2.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
resultados_formateados_zona2.saveAsTextFile("medicionesdiarias_zona2.csv")

resultados_formateados_zona3 = resultados_formateados_zona3.groupByKey().map(lambda x : (x[0],list(x[1])))
resultados_formateados_zona3 = resultados_formateados_zona3.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
resultados_formateados_zona3.saveAsTextFile("medicionesdiarias_zona3.csv")

resultados_formateados_zona4 = resultados_formateados_zona4.groupByKey().map(lambda x : (x[0],list(x[1])))
resultados_formateados_zona4 = resultados_formateados_zona4.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
resultados_formateados_zona4.saveAsTextFile("medicionesdiarias_zona4.csv")

resultados_formateados_zona5 = resultados_formateados_zona5.groupByKey().map(lambda x : (x[0],list(x[1])))
resultados_formateados_zona5 = resultados_formateados_zona5.map(lambda tupla: tupla[0] + ';' + ';'.join(str(d) for d in tupla[1]))
resultados_formateados_zona5.saveAsTextFile("medicionesdiarias_zona5.csv")


#OUTPUT de todo junto: mes/dia/anyo;cant_no2_estacionX;cant_no2_estacionY;...;cant_no2_estacionN
# 01/01/2017;50;53;...
# 01/02/2017;62;64;...
# ...
