numero = int(input("Ingrese el número para la tabla de multiplicar: "))
multiplo = 1
while multiplo <= 10:
    resultado = numero * multiplo
    print(f"{numero} x {multiplo} = {resultado}")
    multiplo += 1