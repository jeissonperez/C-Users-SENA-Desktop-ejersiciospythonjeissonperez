#se le pide al usuario que digite la cantidad de llantas que quiere comprar
llantas=int(input("ingrese la cantidad de llantas que desea comprar: "))
#si la cantidad de llantas es menor a 5 el precio seria 300000
if llantas<5:
    precio=300000
#se la cantidad de llantas esmayor o igual a 5 y menor o igual a 10 el precio sera de 250000
elif 5<=llantas<=10:
    precio=250000
#si no cumple ninguna de las opciones el valor de la llantas seria  de 200000
else:
    precio=200000
#se
total=llantas*precio
print(f"el totala pagar por {llantas} llantas es: ${total}")
