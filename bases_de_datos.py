import pymysql

miconexion = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    database="registros"
)

cur = miconexion.cursor()
cur.execute("SELECT * FROM registros_de_empleados")

datos = cur.fetchall()
for fila in datos:
    print(fila)
