# ejercicio 4 :Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
#digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto.
#-----------------------------------------------------------------------------
#creo las cuentas
sumadeCalificaciones = 0
calificacionmasAlta = 0
calificacionmasBaja = 20
#creo el bucle con limite de 20 que son el numero de estudiantes
for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    sumadeCalificaciones += calificacion #la calificacion puesta se suma al total
    if calificacion > calificacionmasAlta: #si la calificacion puesta supera a la calificacion mas alta esta se remplaza por esta
        calificacionmasAlta = calificacion 
    if calificacion < calificacionmasBaja: #si la calificacion puesta es mas baja que la calificacion mas baja actual esta se remplaza con esta
        calificacionmasBaja = calificacion
#se divide el total de las calificaciones con 20 para sacar el promedio        
promedio = sumadeCalificaciones / 20
#se imprime la calificacon mas alta, mas baja y el promedio
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {calificacionmasAlta:.2f}")
print(f"Calificación más baja: {calificacionmasBaja:.2f}")