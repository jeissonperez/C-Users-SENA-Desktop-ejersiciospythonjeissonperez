# ejercicio 1 :Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
# escribo los contadores de positivo, negativo y neutro
positivo = 0
negativo = 0
neutro = 0

# se Lee los 20 numeros que escribe el usuario
for i in range(20):
    numero = float(input("Ingrese un numero: "))
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    else:
        neutro += 1

# se imprime los resultados de cuales son positivos, negativos y neutros
print("Cantidad de números positivos:", positivo)
print("Cantidad de números negativos:", negativo)
print("Cantidad de números neutros:", neutro)