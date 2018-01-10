"""
Created by Rodrigo de Miguel on 08/01/2018.
"""
import boto3
import time
import datetime

# Let's use Amazon S3
s3 = boto3.resource('s3')


dia = datetime.date.today().strftime("%d/%m/%Y")
hora =  datetime.datetime.now().strftime("%H:%M")

fechaJSON = '{"dia":"'+dia+'","hora":"'+hora+'"}'

data = open('valoresTiempoReal/part-00000', 'rb')
s3.Bucket('bucketcloud18').put_object(Key='Datos Proyecto/Tiempo_real/horario.json', Body=data, ACL='public-read')

s3.Bucket('bucketcloud18').put_object(Key='Datos Proyecto/Tiempo_real/fechaActualizacion.json', Body=fechaJSON, ACL='public-read')