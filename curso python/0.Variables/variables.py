
# phyton tiene siertas palabras reservadas
# se puede usar lo siguiente para varificar si esta reservada o no
# >>> import keyword
# >>> keyword.iskeyword('nombre de la variable')

# las variables son identificadores para cualquier tipo de dato
# estas a la vez deben ser unicas 

# Reglas
# -usar las variables en minuscula
# -nunca usar simbolos especiales
# -el primer caracter no puede se un numero oi digito
# -las constantes son colocadas dentro de módulos Python y significa que no puede ser cambiado
# -los nombres de constante y variable debería tener la combinación de letras en 
#  minúsculas (de a a la z) o MAYÚSCULAS (de la A a la Z) o dígitos (del 0 al 9) o un underscore (_)
# -los nombres que comienzan con guión bajo (simple _ o doble __) se reservan para variables 
#  con significado especial

# Nomenclatura Dinamixa
# esto se refiere a que puedes re-asignar variables a otros tipos de datos
# como por ejemplo
# mis_cosas = 2
# mis_cosas =  ["casa", "perro"]

# para usarse simplemente se las llama por su nombre 
# ejemplo
variable = "soy una variable"
print(variable)

# Variables Locales
# estas soon definidas y utilizadas en el bloque de codigo de una funcion
# y solo existen dentro de la misma
# a su vez, las variables existentes fuera de una función, no son visibles dentro de la misma
# ejemplo
x = 10

def probando():
    x = 11
    return print(x)

probando()
print(x)

# Variables Globales
# una variable local puede convertirse en una variable global declarándola explícitamente 
# como tal con la sentencia 'global'
# de esta forma podemos usarla sin importar el nivel
# ejemplo

coso = "variable anterior"

def modificar_variable():
    global coso
    coso = "variable modificada"

print(coso)
modificar_variable()
print(coso)


################################################################################################