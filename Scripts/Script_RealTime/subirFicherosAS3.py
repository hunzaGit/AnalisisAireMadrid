"""
Created by Rodrigo de Miguel on 08/01/2018.
"""
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

data = open('valoresTiempoReal/part-00000', 'rb')
s3.Bucket('bucketcloud18').put_object(Key='Datos Proyecto/Tiempo_real/horario.json', Body=data, ACL='public-read')

