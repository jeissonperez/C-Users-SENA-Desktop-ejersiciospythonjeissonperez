#ejercicio 6: Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
#total de n personas.
#-------------------------------------------------------------------------
#  se escribe los contadores
numeroPersonas = int(input("Introduce el número total de personas en el salón: "))
contadorHombres = 0
contadorMujeres = 0
contadorActual = 0

# creo un bucle que se limite segun el numero de persona que haya puesto el usuario
while contadorActual < numeroPersonas:
    # se Solicitar el género de la persona
    genero = input("Introduce el género de la persona (hombre/mujer): ")
    
    if genero == "hombre": #si el genero es hombre se suma a su contador
        contadorHombres += 1
    elif genero == "mujer": #si es mujer se suma a su contador
        contadorMujeres += 1
    else:
        print("Género no válido. Introduce 'hombre' o 'mujer'.")
        continue  #se Vuelve a preguntar si el género no es el correcto
    
    # Incrementar el contadoractual para que llegue a su limite
    contadorActual += 1

# se imprime los resultados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")
