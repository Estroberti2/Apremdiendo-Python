# Con el bucle for podemos ejecutar un conjunto de declaraciones, 
# una vez para cada elemento de una lista, tupla, conjunto, etc.

# ejemplo:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# ejemplo:

for x in "banana":
  print(x)


# Sentencia 'continue'
# Con la instrucción continue podemos detener la iteración actual 
# del ciclo y continuar con la siguiente

# ejemplo:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# Sentencia 'range(inicio, fin, pasos)'
# devuelve una secuencia de números, comenzando desde 0 de forma predeterminada, 
# se incrementa en 1 (de forma predeterminada) y termina en un número especificado.
# este mismo no incluye al numero final

# ejemplo:

for x in range(2, 11, 2):
  print(x)


# Sentencia 'break'
# permite finalizar el bucle

# ejemplo:

for x in range(6):
    if x == 3: break
    print(x)

print("Finally finished!")


# Sentencia 'pass'
# en el caso de que tengas un bucle vacio
# 'pass' te ayuda a ejecutarlo sin mostrar el error

# ejemplo:

for x in [0, 1, 2]:
    pass


