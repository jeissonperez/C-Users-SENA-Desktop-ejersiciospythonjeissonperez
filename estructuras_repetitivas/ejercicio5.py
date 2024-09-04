#ejercicio 5 :Una persona debe realizar un muestreo con 50 personas para determinar el
#promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
#Las categorías se determinar de acuerdo a la siguiente tabla:
#---------------------------------------------------------------------------------
# creo los contadores para almacenar las sumas de pesos y los conteos
sumaPesosNiños = 0
conteoNiños = 0

sumaPesosJovenes = 0
conteoJovenes = 0

sumaPesosAdultos = 0
conteoAdultos = 0

sumaPesosAncianos = 0
conteoAncianos = 0

# Bucle con limite de 50 personas y le pido al usuario su edad y peso
for i in range(50):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    peso = float(input(f"Ingrese el peso de la persona {i+1}: "))

    # se le añade a las cuentas segun sus pesos y conteo según la edad
    if edad <= 12: #si es menor o igual de doce el peso se le suma al peso total de los niños y se aumenta 1 niño al conteo de los niños
        sumaPesosNiños += peso
        conteoNiños += 1
    elif edad <= 29: #si es menor o igual de 29 el peso se le suma al peso total de jovenes y se aumenta 1 joven al conteo de jovenes
        sumaPesosJovenes += peso
        conteoJovenes += 1
    elif edad <= 59: #si es menor o igual de 59 el peso se le suma al peso total de adultos y se aumenta 1 adulto al conteo de adultos
        sumaPesosAdultos += peso
        conteoAdultos += 1 
    else: #si no cumple ninguna de estas es menor de 59 el peso se le suma al peso total de ancianos y se aumenta 1 anciano al conteo de ancianos
        sumaPesosAncianos += peso
        conteoAncianos += 1

# Cálculo la presentación de promedios directamente
if conteoNiños > 0: #si el conteo de niños es mayor que cero, el total de pesos de los niños se le dividira con el conteo de los niños para sacar el promedio
    promedioNiños = sumaPesosNiños / conteoNiños
    print(f"Promedio de peso en la categoría Niños: {promedioNiños:.2f} kg")
else: #si no cumple se imprimira el mensaje de que no hay datos para calcular osea que no hay niños
    print("No hay datos para calcular el promedio en la categoría Niños")

if conteoJovenes > 0: #si el conteo de jovenes es mayor que cero, el total de pesos de los jovenes se le dividira con el conteo de los jovenes para sacar el promedio
    promedioJovenes = sumaPesosJovenes / conteoJovenes
    print(f"Promedio de peso en la categoría Jóvenes: {promedioJovenes:.2f} kg")
else: #si no cumple se imprimira el mensaje de que no hay datos para calcular osea que no hay jovenes
    print("No hay datos para calcular el promedio en la categoría Jóvenes")

if conteoAdultos > 0: #si el conteo de adultos es mayor que cero, el total de pesos de los adultos se le dividira con el conteo de los adultos para sacar el promedio
    promedioAdultos = sumaPesosAdultos / conteoAdultos
    print(f"Promedio de peso en la categoría Adultos: {promedioAdultos:.2f} kg")
else: #si no cumple se imprimira el mensaje de que no hay datos para calcular osea que no hay adultos
    print("No hay datos para calcular el promedio en la categoría Adultos")

if conteoAncianos > 0: #si el conteo de ancianos es mayor que cero, el total de pesos de los ancianos se le dividira con el conteo de los ancianos para sacar el promedio
    promedioAncianos = sumaPesosAncianos / conteoAncianos
    print(f"Promedio de peso en la categoría Ancianos: {promedioAncianos:.2f} kg")
else: #si no cumple se imprimira el mensaje de que no hay datos para calcular osea que no hay ancianos
    print("No hay datos para calcular el promedio en la categoría Ancianos")
