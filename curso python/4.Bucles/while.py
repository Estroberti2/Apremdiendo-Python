# El ciclo 'while' nos permite realizar múltiples iteraciones basándonos en el resultado 
# de una expresión lógica que puede tener como resultado un valor 'True' o 'False'

# ejemplo:

contador = 1
while (contador <=10):
    print(contador)
    contador+=1

# en el ejemplo vemos como mientras se cumpla la sentencia (contador <= 10)
# y deja de ejecutar cuando no


# Bucle 'whilw-else'
# tambien puede usarse una sentencia 'else' despues de un 'while' 
# este 'else' mantiene su estructura sin cambios
# de esta forma mientras se cumpla la funcion 'while' hara una cosa y cuando 
# ya no se cumpla continuara con el 'else'

# ejemplo: mostrar promedio de numeros dados

print("Ingrese un numero ('f' para finalizar)")
numero = input()
total = 0
contador = 0

while numero != 'f':
    numero = int(numero)
    #global total
    total += numero
    #global contador
    contador += 1
    print("Ingrese un numero ('f' para finalizar)")
    numero = input()
else:
    if total == 0:
        print ("El promedio es: 0")
    else:
        promedio = total / contador
        print ("El promedio es: " + str(promedio))


# como vemos en el ejemplo se seguira ejecutanto el 'while' como si fueran un
# iterador de if hasta que el usuario ingrese 'f'


# Sentencia 'break'
# esta sirve para finalizar el iterador por la fuerza 
# este generalmente viene dentro de un condicional para indicar cuando va a usarse

# ejemplo: mostrar numeros hasta el 5 y romper

variable = 0

while variable >= 0:
    print("Actual valor de variable: " + str(variable))

    if variable == 5:
        break
    
    variable = variable + 1


# Sentencia 'continue'
# hace que si se cumple la sentencia 
# todo lo que esta despues no se ejecute y pase a la siguiente iteracion

# ejemplo: numeros pares del 1 al 10

i = 1
while i <= 10:
    if (i % 2) != 0:
        continue
    else:
        print (i)
        i += 1

