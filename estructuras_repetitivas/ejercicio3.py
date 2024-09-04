# ejercicio 3:Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
# Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja de todo el grupo
#-------------------------------------------------------------------------
#le pido al usuario que escriba el numero para la tabla de multiplicar
numero = int(input("Ingrese el número para la tabla de multiplicar: "))
#añado el multiplo 1 que sera con el que se multiplicara el numero que el usuario haya puesto
multiplo = 1
#le añado limite de 10 
while multiplo <= 10:
    resultado = numero * multiplo #se hace la ecuacion de la multiplicacion
    print(f"{numero} x {multiplo} = {resultado}") #se escribe y repite el resultado de todos los numeros
    multiplo += 1 #el multiplo se le suma 1 para que "numero" se multiplique con todos los numeros de 1 a 10