import mysql.connector



conn = mysql.connector.connect(
        host='',
        user= '',
        password= '',
        database= 'example'
)

cursor = conn.cursor()

cursor.execute("select * from db ")

resultado = cursor.fetchall()

for dato in resultado:
    print(dato)
else:
    print("la tabla no tiene datos")

conn.close
