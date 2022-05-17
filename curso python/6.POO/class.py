# PROGRAMACION ORIENTADA A OBJETOS (POO)
# Una clase es una plantilla para crear objetos
# Un objeto es una instancia de una clase

# Los objetos son la clave para entender la POO. Si mira a nuestro alrededor 
# encontrará un sin fin de objetos de la vida real: perro, escritorio, 
# televisor, bicicleta, etc…

# En Python:
# -Todo es un objeto, incluyendo los tipos y clases.
# -Permite herencia múltiple.
# -No existen métodos ni atributos privados.
# -Los atributos pueden ser modificados directamente.
# -Permite «monkey patching».
# -Permite «duck typing».
# -Permite la sobrecarga de operadores.
# -Permite la creación de nuevos tipos de datos.

# La creacion de una clase ('class')

# ejemplo: creamos una clase prueba
class Prueba:
    pass

# Los nombres de las clases se escriben por convención capitalizadas
# Pueden (y siempre deberían) tener comentarios.


# ATRIBUTOS
# Los atributos o propiedades de los objetos son las características que puede tener un objeto
# Si el objeto es 'Persona' los atributos podrían ser: dni, nombre, apellido, sexo, etc…

# ejemplo: atributos Persona

class Persona:
    def __init__(self, dni, nombre, apellido, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo

# Todas las clases tienen una función llamada __init __ (),
#  que siempre se ejecuta cuando se inicia la clase.
# Estas para asignar valores a las propiedades del objeto u otras 
#  operaciones que sean necesarias cuando se crea el objeto

# Ahora para instanciar un objeto Persona
# pasaremos los datos que tiene como argumento

persona1 = Persona(123456789, "Pepe", "Potatcio", "Helicoptero de Combate")


# METODOS
# A las clases se lo puede ademas incorporar comportamientos llamados 'Metodos'
# Estos representan las operaciones que se pueden realizar con los objetos de la clase

# ejemplo: clase Perro con metodo ladrar

class Perro:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color
    def hablar(self):
        print("Wang!")

perro = Perro("rottweiler", "marron")
perro.hablar()


# Modificar un Atributo de un Objeto
# para ello simplemente llamamos a la atributo y le ponemos otro valor

# ejemplo: modificamos el color del perro

perro.color = "Blanco"
print(perro.color)


# Eliminar un Atributo 
# Para ello agregamos la propiedad 'del' y luego llamamos al atributo

# ejemplo: quitamos la raza

del perro.raza
print(perro.raza)


# Se usa la misma sentencia para eliminar un objeto

# ejemplo eliminar perro

del perro
print(perro)