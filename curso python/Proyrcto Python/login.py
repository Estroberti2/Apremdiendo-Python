import getpass
import time
from os import system
from chekin import Checkin

def MenuPrincipal():
    print("..........BIENVENIDOS..........")
    print(".                             .")
    print(".      1) INGRESAR            .")
    print(".      2) NUEVO CLIENTE       .")
    print(".      3) SALIR               .")
    print("...............................")

    opcion = input(".   Opcion:")
    if opcion==1:
        LogIn()
    elif opcion==2:
        # Crear Usuario
        print("2")
    elif opcion==3:
        print("Chausim")
        #system('pause')
        #time.sleep(500)
        exit()
    else:
        system("cls")

    


def LogIn():
    
    print(".     -INGRESE SU MAIL        .")
    mail = input("-:")
    print(".   -INGRESE SU CONTRASEÑA    .")
    contraseña = getpass.getpass("-:")

    check = Checkin
    check.chequear(mail, contraseña)


MenuPrincipal()