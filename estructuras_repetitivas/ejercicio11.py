# ejercicio 11:Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
# se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
# la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
# que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
# sea igual a 0.
# ----------------------------------------------------------------------------------------
# creo los contadores 
mujeres=0


hombres=0


estaturaTotal=0
estaturaMayor=0
estaturaMenor=0
#creo un bucle con el limite de el total de estudiantes
totalEstudiantes=int(input("ingrese el numero de estudiantes: "))
for i in range (totalEstudiantes):
    print(f"estudiante {i+1}")
#pregunto al usario el genrero, edad y su altura
    genero=input("ingrese su genero (hombre/mujer): ")
    edad=int(input("ingrese su edad: "))
    if edad <= 0: #si la edad es menor o igual a cero este imprime un mensaje sobre que la edad no es valida
        print(f"edad no valida, debe ser mayor a cero")
    altura=float(input("ingrese su altura en metros: "))
    if genero == "hombre": #si es hombre este se suma a la cuenta de hombres
        hombres+=1
    elif genero == "mujer": #si es mujer esta se le suma a la cuenta de mujeres
        mujeres+=1
    estaturaTotal+=altura #la altura se le suma a la cuenta total de la estatura no importa su genero
    if altura > 1.70: #si es mayor de 1.70 este se le suma a la cuenta de estatura mayor a 1.70
        estaturaMayor += 1
    elif altura < 1.50: #si es menor de 1.50 este se le suma a la cuenta de estatura menor o igual a 1.50
        estaturaMenor += 1
#realizo la ecuacion para sacar el promedio de la altura del total de estudiantes
alturaPromedio=estaturaTotal/totalEstudiantes
#imprimo los resultados
print(f"---------------------------------------------")
print(f"la cantidad de hombres son: {hombres}")
print(f"la cantidad de mujeres son: {mujeres}")
print(f"la altura promedio es: {alturaPromedio:.2f}")
print(f"la cantidad de alumnos que tienen una altura mayor a 1.70 es: {estaturaMayor}")
print(f"la cantidad de alumnos que tienen una altura menor o igual a 1.50 es: {estaturaMenor}")