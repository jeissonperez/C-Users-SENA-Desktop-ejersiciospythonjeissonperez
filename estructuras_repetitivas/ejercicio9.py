# creo las cuentas de los hombres mujeres y su edad total
total_hombres = 0
edad_hombres = 0

total_mujeres = 0
edad_mujeres = 0

total_alumnos = 0
edad_total = 0

# Número de alumnos
num_alumnos = int(input("¿Cuántos alumnos hay en total? "))

# Recolección de datos y cálculo de promedios
for i in range(num_alumnos):
    print(f"\nAlumno {i+1}")
    genero = input("Ingrese el género (H para hombre, M para mujer): ")
    edad = int(input("Ingrese la edad: "))

    total_alumnos += 1
    edad_total += edad

    if genero == 'H':
        total_hombres += 1
        edad_hombres += edad
    elif genero == 'M':
        total_mujeres += 1
        edad_mujeres += edad

# Cálculo de promedios
promedio_hombres = edad_hombres / total_hombres if total_hombres > 0 else 0
promedio_mujeres = edad_mujeres / total_mujeres if total_mujeres > 0 else 0
promedio_total = edad_total / total_alumnos if total_alumnos > 0 else 0

# Resultados
print(f"\nPromedio de edades de hombres: {promedio_hombres}")
print(f"Promedio de edades de mujeres: {promedio_mujeres}")
print(f"Promedio de edades de todo el grupo: {promedio_total}")