# Análisis Aire Madrid
Proyecto para la asignatura de Cloud Computing and Big Data de la UCM

## Descripción
Se realizará un análisis detallado de compuestos químicos del aire que utiliza el Ayuntamiento de Madrid para poner en marcha los periodoas de restricciones por alta contaminación, comporbando el resultado de dichos periodos a lo largo del año.

Se utilizarán los datos proporcionados por el Ayuntamiento atraves de su [portal de datos abiertos](http://datos.madrid.es/portal/site/egob/) de los contamientes recogidos por las distintas estaciones repartidas por el municipio. Se utilizará Apache Spark para el análisis de datos, utilizando una máquina virtual en Amazon AWS con el servicio EC2 para su procesado y un Bucket S3 para su almacenamiento.

Posteriormente se realizará uan pequeña web para explicar el proceso y los resultados.

## Entorno

 - **Python** 3.3.7
 - **Apache Spark** 2.2.0
 - **AWS EC2** t2.nano
 - **Ubuntu** 16.04 
