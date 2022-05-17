# La sentencia condicional se usa para tomar decisiones,
# este evaluá básicamente una operación lógica, 
# es decir una expresión que de como resultado True o False, 
# y ejecuta la pieza de código siguiente siempre y cuando el resultado sea verdadero

frutaPablo = "pera"
frutaDiego = "pera"

if (frutaDiego == frutaPablo):
    print("Ambos tienen la misma fruta")

# ahi vimos la sentencia 'if'

verduraDiego = "zapallo"
verduraPablo = "anco"

if (verduraDiego == verduraPablo):
    print("Ambos tienen la misma fruta")
else:
    print("La fruta es diferente")

# ahi usamos la sentencia 'if- else'

numero1 = 22
numero2 = 33

if (numero1 > numero2):
    print("numero1 es mayor")
elif (numero1 < numero2):
    print("numero2 es mayor")
else:
    print("Son Iguales")

# ahi usamos la sentencia 'if-elif-else'