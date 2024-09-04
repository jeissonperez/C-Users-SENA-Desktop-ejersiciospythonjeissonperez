numeroAutos=int(input("ingrese el numero de autos: "))
amarilla= 0
rosa = 0
roja = 0
verde = 0
azul = 0
#uso un bucle con limite de 50 
for i in range(numeroAutos):
    colorCalcomania=int(input(f"Ingrese el ultimo numero de la {i+1} placa: "))
 #uso append para que el peso se le agrege a la lista segun la edad
    if colorCalcomania == 3 or colorCalcomania == 4:
        rosa += 1
    elif colorCalcomania == 5 or colorCalcomania == 6:
        roja += 1
    elif colorCalcomania == 7 or colorCalcomania == 8:
        verde += 1
    elif colorCalcomania == 1 or colorCalcomania == 2:
        amarilla += 1
    elif colorCalcomania == 9 or colorCalcomania == 0:
        azul += 1
    else:
        print("usted ingreso un digito erroneo por favor ingrese otro")
#uso def para sacar la definicion de esta funcion y calculo el promedio de el peso
print(f"----------------------------------------------------------")
print(f"la cantidad de autos con calcomania amarilla son:{amarilla} ")
print(f"la cantidad de autos con calcomania rosa son:{rosa} ")
print(f"la cantidad de autos con calcomania roja son:{roja} ")
print(f"la cantidad de autos con calcomania verde son:{verde} ")
print(f"la cantidad de autos con calcomania azul son:{azul}")
    
