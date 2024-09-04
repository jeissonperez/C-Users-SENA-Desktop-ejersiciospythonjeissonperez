#ejercicio 7: La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad
#de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo
#dígito de la placa de cada carro, se puede determinar el color de la calcomanía
#utilizando la siguiente relación: 
#------------------------------------------------------------------------------------
# agrego los contadores y le pregunto al usuario el numero de autos
numeroAutos=int(input("ingrese el numero de autos: "))
amarilla= 0
rosa = 0
roja = 0
verde = 0
azul = 0
#uso un bucle con limite el numero de autos que haya ingresado el usuario
for i in range(numeroAutos):
    colorCalcomania=int(input(f"Ingrese el ultimo numero de la {i+1} placa: "))
 #segun el numero final de la placa se suma a su respectivo color
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
#se imprime el numero total de calcomanias de cada color
print(f"----------------------------------------------------------")
print(f"la cantidad de autos con calcomania amarilla son:{amarilla} ")
print(f"la cantidad de autos con calcomania rosa son:{rosa} ")
print(f"la cantidad de autos con calcomania roja son:{roja} ")
print(f"la cantidad de autos con calcomania verde son:{verde} ")
print(f"la cantidad de autos con calcomania azul son:{azul}")
    
