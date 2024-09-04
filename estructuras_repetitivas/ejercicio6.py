# Inicialización
num_personas = int(input("Introduce el número total de personas en el salón: "))
contador_hombres = 0
contador_mujeres = 0
contador_actual = 0

# Bucle para procesar cada persona
while contador_actual < num_personas:
    # Solicitar el género de la persona
    genero = input("Introduce el género de la persona (hombre/mujer): ").strip().lower()
    
    # Actualizar los contadores
    if genero == "hombre":
        contador_hombres += 1
    elif genero == "mujer":
        contador_mujeres += 1
    else:
        print("Género no válido. Introduce 'hombre' o 'mujer'.")
        continue  # Volver a preguntar si el género no es válido
    
    # Incrementar el contador de personas procesadas
    contador_actual += 1

# Mostrar los resultados
print(f"Cantidad de hombres: {contador_hombres}")
print(f"Cantidad de mujeres: {contador_mujeres}")
