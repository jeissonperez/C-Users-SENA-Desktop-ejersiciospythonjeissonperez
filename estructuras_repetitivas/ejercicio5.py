import random

categorias = {
    'Niños': (0, 12),
    'Jóvenes': (13, 29),
    'Adultos': (30, 59),
    'Ancianos': (60, 100)
}

pesos = {categoria: [] for categoria in categorias}

for _ in range(50):
    edad = random.randint(0, 100)
    peso = random.uniform(20.0, 100.0)
    for categoria, (edad_min, edad_max) in categorias.items():
        if edad_min <= edad <= edad_max:
            pesos[categoria].append(peso)

for categoria, lista_pesos in pesos.items():
    promedio_peso = sum(lista_pesos) / len(lista_pesos) if lista_pesos else 0
    print(f"Promedio de peso en la categoría {categoria}: {promedio_peso:.2f} kg")
