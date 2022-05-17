# def es una funcion 

# Una función es un bloque de código con un nombre asociado
# Recibe cero o más argumentos como entrada
# Sigue una secuencia de sentencias, la cuales ejecuta una operación deseada 
# Devuelve un valor o solo realiza una tarea
# Esto puede ser llamados cuando se necesite

# ejemplo: 

def my_funcion():
    print("mi primer funcion")

my_funcion()

# Para ejecutar la funcion solo deve llamarse y pasarle los argumentos

# ejemplo: de 2 parametros

def imprime_nombre(nombre, apellido):
    print(nombre + " " + apellido)

imprime_nombre("renzo", "martinez")


# Cuando no sabes la cantidad de atgumentos que pasaran
# Se agrega en argumento '*nombreTupla' 
# Esto crea una tupla y la podemos recorrer

# ejemplo: lista de nombres

def  lista_nombres(*nombres):
    for nombre in nombres:
        print(nombre)

lista_nombres("juan", "Pedro", "Ezequiel")


# Para recibir elementos de tipo clave-valor (diccionarios)
# se debe agregar en argumentos '**nombreDiccionario'
# esto crea un diccionario ylo podemos recorrer

# ejemplo:

def caracteristicas_personaje(**caracteristicas):
    for caracteristica in caracteristicas:
        print(caracteristica, ":", caracteristicas[caracteristica])

caracteristicas_personaje(nombre = "Harry", vida = 100, atque = 10, defensa = 10)


# Para retornar algo de la funcion
# Simplemente usamos 'retur' y luego le agregamos lo que vamos a devolver

# ejemplo:

def sumar_cinco(x):
      return x + 5

print(sumar_cinco(3))


# Recursividad
# Esto significa que una función definida puede llamarse a sí misma
# Se debe tener mucho cuidado con la recursividad
# Al  ser bastante fácil escribir  se puede terminar con una función que nunca termina,
# o una que usa cantidades excesivas de memoria o potencia del procesador

# ejempolo: contador

def contar_a_cero(i):
    if i > 0:
        print(i)
        i -= 1
        contar_a_cero(i) 
    else:
        print("Cuenta Atras Finalizada")

contar_a_cero(3)