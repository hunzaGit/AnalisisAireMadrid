"""
Created by Rodrigo de Miguel on 08/01/2018.
"""

from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('valoresTiempoReal')
sc = SparkContext(conf = conf)

#											              8     9    10     11   
# ['28','079','4','1','28079004_1_38','2018','01','08','00001','V','00000','N',....]
def formatearHoras(line):
	tupla = ()
	comunid = line[0]
	municipio = line[1]
	hora = 1
	estacion = line[2]
	# print len(line) # 56
	if len(estacion) == 1:
		estacion = '00' + estacion
	if len(estacion) == 2:
		estacion = '0' + estacion
	for i in xrange(9, len(line), 2):
		# print i
		if line[i] == 'N':
			# print "encontrada una N"
			tupla = ( comunid + municipio + estacion, (line[i - 3], str(hora-1)))
			# print tupla
			return tupla
		elif i == len(line)-1:
			# print "final de linea"
			tupla = ( comunid + municipio + estacion, (line[i - 1], str(hora-1)))
			# print tupla
			return tupla
		else:
			hora += 1
			# print "hora: " + str(hora)



# ('codEstacion', valor, hora)


rdd = sc.textFile("horario.csv")
# Madrid, xxxx, estacion, parametro, tecnica, periodo, anyo, mes, valores....
# 28,079,004,01,38,04,2017,01,00006,V,00008,V,00012,V,.....

header = rdd.first()
# userId,movieId,rating,timestamp

rdd = rdd.filter(lambda line: line!=header)
# 1,31,2.5,1260759144


lines = rdd.map(lambda line: line.encode("ascii", "ignore").split(";"))
# [[line],[line],...]  -- Lineas con comas
# ['28','079','4','1','28079004_1_38','2018','01','08','00001','V',....]


linesNO2 = lines.filter(lambda line: line[3] == '8')
# ['28','079','4','8','28079004_1_38','2018','01','08','00001','V',....]



linesF = linesNO2.map(formatearHoras)
# ('codEstacion', (valor, 'hora'))


linesOrd = linesF.sortByKey()
# ('codEstacion', valor, 'hora')

def toJSON(tupla):
	if tupla[0] == '28079004': # primera estacion
		line = '{"'+tupla[0]+'":{"valor":"'+tupla[1][0]+'", "hora":"'+tupla[1][1]+'"},'
	elif tupla[0] == '28079060': # ultima estacion
		line = '"'+tupla[0]+'":{"valor":"'+tupla[1][0]+'", "hora":"'+tupla[1][1]+'"}'+'}'
	else:
		line = '"'+tupla[0]+'":{"valor":"'+tupla[1][0]+'", "hora":"'+tupla[1][1]+'"},'
	return line


linesJSON = linesOrd.map(toJSON)
# "codEstacion":{ "valor": "valor",  "hora": "hora" }

linesJSON.saveAsTextFile("valoresTiempoReal")