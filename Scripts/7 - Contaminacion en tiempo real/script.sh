#!/bin/bash

# Created by Rodrigo de Miguel on 08/01/2018.
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/sbin:/usr/sbin:/sbin

echo --------------------------------------------------------------------------
date
echo --------------------------------------------------------------------------
echo
echo --- Descargando fichero...

curl -O http://www.mambiente.munimadrid.es/opendata/horario.csv

echo --- Eliminando directorio...

# rm -r ~/rodrigoDir/proyecto/tiemporeal/valoresTiempoReal/
rm -r valoresTiempoReal/

echo --- Ejecutando Spark..

/home/ubuntu/spark-2.2.0-bin-hadoop2.7/bin/spark-submit tiemporeal.py

echo --- Subiendo fichero a AWS S3

python subirFicherosAS3.py 

echo --- Terminado!
echo --------------------------------------------------------------------------
echo