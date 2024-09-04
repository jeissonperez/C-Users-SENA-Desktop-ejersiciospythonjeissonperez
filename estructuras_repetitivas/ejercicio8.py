#un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
#algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
#imprima:
#• La cantidad de estudiantes que obtuvieron una calificación menor a 50.
#• La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70.
#• La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.
#• La cantidad de estudiantes que obtuvieron una calificación de 80 o más
#----------------------------------------------------------------------------
#creo los contadores de los estudiantes
estudiantesMenor50=0
estudiantes_50_70=0
estudiantes_70_80=0
estudiantes_80_100=0
#uso un bucle de limite 23 que son los numeros de estudiantes y le pido la primera nota del primer estudiante
for i in range(23):
    calificacion=int(input(f"Ingrese su {i+1} nota obtenida: "))
 #segun la nota se suma a la cuenta segun su resultado
    if calificacion < 50 and calificacion >= 0:
        estudiantesMenor50 += 1
    elif calificacion >= 50 and calificacion < 70:
        estudiantes_50_70 += 1
    elif calificacion >= 70 and calificacion < 80:
        estudiantes_70_80 += 1
    elif calificacion >= 80 and calificacion < 100:
        estudiantes_80_100 += 1
    else:
        print("usted ingreso un digito erroneo por favor ingrese otro")
#se imprime el numero total de estudiantes de cada valor
print(f"----------------------------------------------------------")
print(f"La cantidad de estudiantes que obtuvieron una calificación menor a 50 son:{estudiantesMenor50} ")
print(f"La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 70 son:{estudiantes_50_70} ")
print(f"La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80 son:{estudiantes_70_80} ")
print(f"La cantidad de estudiantes que obtuvieron una calificación de 80 o más son:{estudiantes_80_100} ")

    