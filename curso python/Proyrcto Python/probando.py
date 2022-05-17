import pymysql

mail = "@mail.com"
contrasenia = "caca"

conexion = pymysql.connect(host='localhost',
                                  user='root',
                                  password='',
                                  db='Tienda')

cursor = conexion.cursor()

sql = "SELECT mail FROM usuarios;"

cursor.execute(sql)

resultado = cursor.fetchall()

print(len(resultado)==0)

conexion.close()