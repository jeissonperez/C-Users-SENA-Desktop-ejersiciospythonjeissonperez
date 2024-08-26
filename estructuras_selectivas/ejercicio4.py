totalDeLaCompra=float(input("digites el total de su compra: "))
color=input("digite el color de su boleta: ")
if color=="rojo":
    descuento=0.15
elif color=="verde":
    descuento=0.20
else:
    descuento=0.0
valorDescuento=totalDeLaCompra*descuento
valorAPagar=totalDeLaCompra-valorDescuento
print(f"el valor de su compra fue: ${totalDeLaCompra:.2f}")
print(f"el color de su balota fue: ${color}")
print(f"el descuento fue de: ${valorDescuento:.2f}")
print(f"el valor a pagar es de: ${valorAPagar:.2f}")