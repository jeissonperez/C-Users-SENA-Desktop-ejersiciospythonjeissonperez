# Solicita al usuario si desea ingresar la edad del paciente en meses o en años y convierte la entrada a minúsculas
tipoDato = str(input("Desea agregar la edad del paciente en meses o en años?: ")).lower()

# Solicita al usuario la edad del paciente y la convierte a entero
edad = int(input("¿Qué edad tiene el paciente?: "))

# Solicita al usuario el sexo del paciente y lo convierte a minúsculas
sexo = input("El paciente es hombre o mujer?: ").lower()

# Verifica si la entrada para tipoDato es válida
if tipoDato not in ["años", "meses"]:
    # Imprime un mensaje de error si la entrada no es "años" ni "meses"
    print("Entrada inválida. Por favor, ingrese 'Años' o 'Meses'.")
    exit  # Finaliza el programa si la entrada es inválida

# Convierte la edad a meses si el tipoDato es 'años'
if tipoDato == "años":
    convertMonths = edad * 12  # Convierte la edad en años a meses
    # Solicita el nivel de hemoglobina en gramos por decilitro (g%)
    nivelHemoglobina = float(input("Que nivel de hemoglobina ejerce el paciente? inserte el dato en g%: "))
else:
    # Si la edad ya está en meses, se asigna directamente
    convertMonths = edad
    # Solicita el nivel de hemoglobina en gramos por decilitro (g%)
    nivelHemoglobina = float(input("Que nivel de hemoglobina ejerce el paciente? inserte el dato en g%: "))

# Determina el rango mínimo de hemoglobina basado en la edad en meses
if convertMonths >= 0 and convertMonths <= 1:
    rangoMin = 13  # Rango mínimo de hemoglobina para edades entre 0 y 1 mes
elif convertMonths > 1 and convertMonths <= 6:
    rangoMin = 10  # Rango mínimo de hemoglobina para edades entre 1 y 6 meses
elif convertMonths > 6 and convertMonths <= 12:
    rangoMin = 11  # Rango mínimo de hemoglobina para edades entre 6 y 12 meses
elif convertMonths > 12 and convertMonths <= 60:  # 1 año = 12 meses, 5 años = 60 meses
    rangoMin = 11.5  # Rango mínimo de hemoglobina para edades entre 1 y 5 años
elif convertMonths > 60 and convertMonths < 120:  # 10 años = 120 meses
    rangoMin = 12.6  # Rango mínimo de hemoglobina para edades entre 5 y 10 años
elif convertMonths >= 120 and convertMonths <= 180:  # 15 años = 180 meses
    rangoMin = 13  # Rango mínimo de hemoglobina para edades entre 10 y 15 años
else:
    # Si la edad del paciente es mayor a 15 años, ajusta el rango mínimo según el sexo
    if sexo == "mujer" and convertMonths > 180:
        rangoMin = 12  # Rango mínimo de hemoglobina para mujeres mayores de 15 años
    elif sexo == "hombre" and convertMonths > 180:
        rangoMin = 14  # Rango mínimo de hemoglobina para hombres mayores de 15 años

# Determina si el paciente tiene anemia comparando el nivel de hemoglobina con el rango mínimo
if nivelHemoglobina < rangoMin:
    resultado = "Positivo para anemia"  # El nivel de hemoglobina es menor que el rango mínimo, indicando anemia
else:
    resultado = "Negativo para anemia"  # El nivel de hemoglobina es igual o mayor que el rango mínimo, indicando ausencia de anemia

# Imprime el resultado del análisis
print("Resultado:", resultado)
