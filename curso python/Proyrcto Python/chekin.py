import pymysql

class Checkin:
    #def __init__(self):
        # try:
	    #     conexion = mysql.connect(host='localhost', user='root', password='', db='Tienda')
        #     except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        #     print("Ocurrió un error al conectar: ", e)
    @staticmethod
    def chequear(mail, contraseña):
        # self.mail = mail
        # self.contraseña = contraseña
        conexion = pymysql.connect(host='localhost',
                                  user='root',
                                  password='',
                                  db='Tienda')

        cursor = conexion.cursor()

        sqlCliente = "select num_cliennte from clientes where dni in (select dni from informacion where id_usuario in (select id_usuario from usuarios where mail="+mail+" and contraseña="+contraseña+"));"
        print(sqlCliente)
        sqlPersonal = "select num_empleado, puesto from clientes where dni in (select dni from informacion where id_usuario in (select id_usuario from usuarios where mail="+mail+" and contraseña="+contraseña+"));"
        print(sqlPersonal)
        cursor.execute(sqlCliente)
        resultado = cursor.fetchall()

        if len(resultado)==0:
            cursor.execute(sqlPersonal)
            resultado = cursor.fetchall()
            if len(resultado[0])==0:
                print("Usuario no Encontrado")
                conexion.close()
            else:
                if resultado[1]=="empleado":
                    conexion.close()
                    # redirijir al menu empleado
                else:
                    conexion.close()
                    # redirigir al menu dueño
        else:
            conexion.close()
        
