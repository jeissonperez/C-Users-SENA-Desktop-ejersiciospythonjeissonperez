zapatillas=int(input("digite el numero de zapatillas compradas "))
if zapatillas==1:
    zapatilla1=int(input("digite el costo de la zapatilla "))
    total=zapatilla1
elif zapatillas==2:
    zapatilla1=int(input("digite el costo de la primera zapatilla "))
    zapatilla2=int(input("digite el costo de la segunda zapatilla "))
    total=zapatilla1+zapatilla2
elif zapatillas==3:
    zapatilla1=int(input("digite el costo de la primera zapatilla "))
    zapatilla2=int(input("digite el costo de la segunda zapatilla "))
    zapatilla3=int(input("digite el costo de la tercera zapatilla "))
    total=zapatilla1+zapatilla2+zapatilla3
elif zapatillas==4:
    zapatilla1=int(input("digite el costo de la primera zapatilla "))
    zapatilla2=int(input("digite el costo de la segunda zapatilla "))
    zapatilla3=int(input("digite el costo de la tercera zapatilla "))
    zapatilla4=int(input("digite el costo de la cuarta zapatilla "))
    total=zapatilla1+zapatilla2+zapatilla3+zapatilla4
elif zapatillas==5:
    zapatilla1=int(input("digite el costo de la primera zapatilla "))
    zapatilla2=int(input("digite el costo de la segunda zapatilla "))
    zapatilla3=int(input("digite el costo de la tercera zapatilla "))
    zapatilla4=int(input("digite el costo de la cuarta zapatilla "))
    zapatilla5=int(input("digite el costo de la quinta zapatilla "))
    total=zapatilla1+zapatilla2+zapatilla3+zapatilla4+zapatilla5
else:
    print("digite otro numero")
if zapatillas >= 3:
    descuento=total*0.20
else:
    descuento=total*0.10
totalApagar=total-descuento
print(f"su total a pagar con el descuento aplicado es {totalApagar}")
print(f"su total a pagar sin el descuento era de {total}")
print(f"su descuento es de {descuento}")


    
    
    

    

   
    
