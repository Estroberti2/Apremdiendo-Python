import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Tienda')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT id_sucursal, nom_sucursal FROM sucursal;")
 
			# Con fetchall traemos todas las filas
			sucursales = cursor.fetchall()
 
			# Recorrer e imprimir
			for sucursal in sucursales:
				print(" id_sucursal: ", sucursal[0], "\n", "nom_sucursal: ", sucursal[1])
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)