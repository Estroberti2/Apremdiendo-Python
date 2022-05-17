# vestas funciones nacen de reducir la funcion
# hasta hacerla sensilla

# ejemplo: funcion

def doblar(numero):
    resultado = numero*2
    return resultado

print(doblar(2))

# ejemplo: reducida

doblar = lambda numero: numero*2

print(doblar(3))


# Este tipo de funciones tambien sirven para otras cosas

# ejemplo: operacion aritmetica 

es_impar = lambda numero: numero%2 != 0
print(es_impar(5))

# ejemplo: texto

revertir_texto = lambda cadena: cadena[::-1]
print(revertir_texto("Telefono"))

# ejemplo: varios parametros

sumar = lambda x,y: x+y
print(sumar(5, 5))