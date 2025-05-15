import mysql.connector
import csv
import boto3

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="mysql_c",  #nombre del contenedor de postgres
    user="utec",
    password="utec",
    database="universidad"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM empleados")
registros = cursor.fetchall()

# Guardar en CSV
nombre_csv = "empleados.csv"
with open(nombre_csv, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["id", "nombre", "puesto", "salario"])  
    writer.writerows(registros)

cursor.close()
conexion.close()

# Subir a S3
nombre_bucket = "paris-output-01"  
s3 = boto3.client('s3')
s3.upload_file(nombre_csv, nombre_bucket, nombre_csv)

print("Ingesta desde MySQL completada.")
