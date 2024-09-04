#escribo las cuentas de 
sumadeCalificaciones = 0
calificacionmasAlta = 0
calificacionmasBaja = 20
for i in range(20):
    calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
    sumadeCalificaciones += calificacion
    if calificacion > calificacionmasAlta:
        calificacionmasAlta = calificacion
    if calificacion < calificacionmasBaja:
        calificacionmasBaja = calificacion
promedio = sumadeCalificaciones / 20
print(f"Promedio de calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {calificacionmasAlta:.2f}")
print(f"Calificación más baja: {calificacionmasBaja:.2f}")