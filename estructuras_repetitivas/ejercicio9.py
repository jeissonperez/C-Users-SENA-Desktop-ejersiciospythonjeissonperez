# ejercicio 9: Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos. 
#---------------------------------------------------------------------------------------------
# creo los contadores
totalhombres= 0
edadTotalHombres= 0


totalMujeres= 0
edadTotalMujeres= 0


totalEstudiantes= 0
edadTotalEstudiantes= 0
#le pregunto al usuario el numero total de alumnos y este sera el limite del bucle
numeroAlumnos=int(input("ingrese el numero de estudiantes en total: "))
for i in range (numeroAlumnos):
    print(f"alumno {i+1}")
#le pregunto al usuario su genero y edad
    genero=input("escriba su genero (hombre/mujer): ")
    edad=int(input("escriba su edad: "))
    totalEstudiantes += 1 #el total de estudiantes se aumenta 1 cada vez que se repita indicando el total de estudiantes y la edad se suma a la edad total de estudiantes
    edadTotalEstudiantes += edad
    if genero == "hombre":#si es hombre el contador de total de hombres se aumenta 1 y la edad se suma a la edad total de hombres
        totalhombres += 1
        edadTotalHombres += edad
    elif genero == "mujer":#si es mujer el contador de total de mujeres se aumenta 1 y la edad se suma a la edad total de mujeres
        totalMujeres += 1
        edadTotalMujeres += edad
#se sacan los promedios de mujeres hombres y el total de los dos
promedioHombres=edadTotalHombres/totalhombres
promedioMujeres=edadTotalMujeres/totalMujeres
promedioEstudiantes=edadTotalEstudiantes/totalEstudiantes
#se imprime el resultado total
print(f"el promedio de edad de los hombres son: {promedioHombres} ")
print(f"el promedio de edad de las mujeres son: {promedioMujeres} ")
print(f"el promedio de edad de todos los estudiantes son: {promedioEstudiantes} ")
