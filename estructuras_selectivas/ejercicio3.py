cantidad=int(input("digite el numero de zapatillas compradas: "))
monto=float(input("digite el costo de la primera zapatilla: "))
montototal=(cantidad*monto)
if montototal>500000:
    propioDinero=montototal*0.55
    prestamo=0.30
    valorCredito=0.15
    print(f"el valor invertido de su propio dinero es {propioDinero:.2f} el valor que pidio al banco es de {prestamo:.2f} y el valor de credito solicitado al fabricante es de {valorCredito:.2f}")
elif montototal<500000:
    propioDinero=montototal*0.70
    valorCredito=montototal*0.30
    intereses=valorCredito*0.20
    totalCredito=valorCredito+intereses
    print(f"el valor invertido de su propio dinero es {propioDinero:.2f} el valor de credito solicitado al fabricante es de {valorCredito:.2f} los intereses del credio son {intereses:.2f} total a pagar por el credito incluyento intereses son {totalCredito}")