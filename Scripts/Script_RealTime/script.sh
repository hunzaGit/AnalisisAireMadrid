#!/bin/bash

# Created by Rodrigo de Miguel on 08/01/2018.

# crontab line
# 31 * * * * ~/rodrigoDir/proyecto/tiemporeal/script.sh

echo Descargando fichero...

curl -O http://www.mambiente.munimadrid.es/opendata/horario.csv

echo eliminando directorio...

rm -r valoresTiempoReal/

echo Ejecutando Spark..

spark-submit tiemporeal.py

echo subiendo fichero a AWS S3

python subirFicherosAS3.py 

echo Terminado!