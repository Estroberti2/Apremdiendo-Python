
# Exsisten 3 tipos de metodos

# Métodos de instancia

# Este es el tipo de método básico y sencillo que utilizará la mayor parte del tiempo
# Estos pueden acceder a la propia clase a través del 'self'
# También pueden modificar el estado de la clase

# ejemplo: foco con metodo que cambie el estado de 'encendido'

class Foco:
    def __init__(self, encender):
        self.encender = encender

    def encender_apagar(self):
        if self.encender == True:
            self.encender = False
        else:
            self.encender = True

foco = Foco(True)
print(foco.encender)
foco.encender_apagar()
print(foco.encender)

         

# Métodos de Clase

# Este se crea incorporando '@classmethod' antes de crear el metodo
# A diferencia del anterior este usa un parametro 'cls' 
# -este 'cls' es la clase
# No puede modificar el estado de la instancia del objeto
# Pero aún pueden modificar el estado de la clase o a todas las instancias
# Estas pueden ser llamadas desde una instancia o la clase

# ejemplo: clase perro con atributo año humano y metodo que devuelva su edad perruna

class Perro:
    def __init__(self, años_humanos):
        self.años_humanos = años_humanos
        self.años_perrunos = años_perrunos

    @classmethod
    def anios_Humanos(cls):
        cls.años_perrunos = cls.años_humanos * 7
        print(cls.años_perrunos)

perro = Perro
perro.años_humanos = 10
perro.anios_Humanos() # Perro.anios_Humanos()



# Métodos Estáticos

# Este no lleva 'self' ni 'dls'
# Puede aceptar todo tipo de parametros
# Se comportan como funciones  simples
# Excepto que  tambien puede llamarlas desde una instancia o la clase

# ejemplo: clase gato con metodo estatico hablar

class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
    @staticmethod
    def hablar():
        print("Miau!!")

Gato.hablar() 