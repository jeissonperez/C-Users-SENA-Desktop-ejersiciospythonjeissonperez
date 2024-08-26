Promedio=float(input("ingrese el promedio del estudiante: "))
pensionBase=float(input("ingrese el valor base de la pension: "))
if Promedio>=4.0:
    valorApagar=pensionBase*0.7
else:
    valorApagar=pensionBase*1.2
print(f"el valor que debe pagar el alumno es: ${valorApagar:.2f}")