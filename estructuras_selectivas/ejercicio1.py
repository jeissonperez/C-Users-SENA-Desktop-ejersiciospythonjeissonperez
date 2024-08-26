calificacion1=int(input("digite su primera calificacion "))
calificacion2=int(input("digite su segunda calificacion "))
calificacion3=int(input("digite su tercera calificacion "))
total=(calificacion1+calificacion2+calificacion3)/3
totalentero=int(total)
print(f"el promedio de los numeros es {totalentero}")
if total>=70:
    print(f"usted aprobo algoritmia con {totalentero}")
elif total<70:
    print(f"usted reprobo algoritmia con {totalentero}")
else :
    print(f"ha digitado algo incorrecto con {totalentero}")





