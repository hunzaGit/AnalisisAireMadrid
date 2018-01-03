"""
Created by Rodrigo de Miguel on 03/01/2018.
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('MediaAnualPorDias')
sc = SparkContext(conf = conf)

#											6	   7      8 	 9
# ['28', '079', '004', '08', '08', '04', '2017', '01', '00050', 'V', '00062', 'V',.....]
def formatearDias(line):
	array = []
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
			array.append(( mes+ '/' + diaStr + '/' + anyo, float(line[i - 1])))
			dia += 1
		else:
			dia += 1
	return array

# ('fecha', valor)


rdd = sc.textFile("datos201711.txt")
# Madrid, xxxx, estacion, parametro, tecnica, periodo, anyo, mes, valores....
# 28,079,004,01,38,04,2017,01,00006,V,00008,V,00012,V,.....


lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(","))
# [[line],[line],...]  -- Lineas con comas
# ['28','079','004','01','38','04','2017','01','00006','V','00008','V','00012','V',.....]


linesNO2 = lines.filter(lambda line: line[3] == '08')
# ['28', '079', '004', '08', '08', '04', '2017', '01', '00050', 'V', '00062', 'V',.....] - solo valores con del NO2

linesNO2 = linesNO2.flatMap(formatearDias)
# ('fecha', valor)


linesNO2Acum = linesNO2.reduceByKey(lambda acum,n: acum+n)
# ['fecha',sumValorTotal] 

# Calcular el mumero de dias de cada anyo
# ------------------------------
numDias = linesNO2.map(lambda tupla: (tupla[0],1))
# ('fecha',1) -- 

numDias = numDias.reduceByKey(lambda acum,n: acum+n)
# ('fecha',numDias) -- Numero de dias contabilizados 
# ------------------------------

joinRDD = linesNO2Acum.join(numDias)
# ('fecha', (sumtotal, numDias)

mediaAnual = joinRDD.map(lambda tupla: (tupla[0], round((tupla[1][0]/tupla[1][1]),2) ) )
# ('fecha', media)

mediaAnual = mediaAnual.sortByKey()

mediaAnual.saveAsTextFile("mediaDias2017")