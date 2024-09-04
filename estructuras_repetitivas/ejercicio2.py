#  ejercicio 2:Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos numeros.
#------------------------------------------------------------------------
#  escribo el contador de la suma de los numeros positivos
sumaNumeros=0
#hago que el bucle se repita 10 veces logrando que el usuario escriba 10 numeros negativos
for _ in range(10):
    while True:
        numero=float(input("escriba un numero negativo"))
        if numero<0:#si el numero es negativo sale del bucle
            break
        else:
            print("el numero que usted ingreso no es negativp por favor ingrese otro")#si no es negativo se le pide al usuario que lo ingrese otra vez
#se convierte el nemero a positivo y se suma a la cuenta
numeroPositivo=-numero
sumaNumeros+=numeroPositivo
#los numero se van sumando a la cunta y se imprime el resultado de la suma de todos los numeros
print(f"la suma de estos numeros es: {sumaNumeros}")

