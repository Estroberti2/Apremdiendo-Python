
# La herencia nos permite definir una clase que hereda todos los métodos y propiedades de otra clase
# Esto hace que no tengamos que escribir todo otra ves

# La herencia se hace creando una clase 'padre'
# Y una clase 'hijo'
# Donde seguido del nombre de la clase hijo ponemos '(nombre clase padre)'

# ejemplo: clase padre persona y clase hijo estudiante

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def persona_saluda(self):
        print("Hola, Soy una Persona")

class Estudiante(Persona): #se indica que Persona es su clase padre
    def __init__(self, nombre, apellido, universidad):
        Persona.__init__(self, nombre, apellido)
        self.universidad = universidad
    def estudiante_saluda(self):
        print("Hola, Soy un Estudiante")

persona = Persona("Eduaard", "Elric")
persona.persona_saluda()

estudiante = Estudiante("Naruto", "Uzumaki", "Sanin")
estudiante.estudiante_saluda()
estudiante.persona_saluda()

# en este caso vemos como un estudiante es tanto un estudiante como una persona