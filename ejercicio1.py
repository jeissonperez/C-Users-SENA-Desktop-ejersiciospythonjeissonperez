mensaje="hola, estoy aprendiendo python"
nombre="jeisson"
formacion="ADSO"
edad="18"
estatura="1.70"
peso="57"
#forma de imprimir 1
print(mensaje,"mi nombre es:",nombre,"soy de la formacion:",formacion,"tengo:",edad,"años","mido:",estatura,"y peso:",peso,"kg")
#forma de imprimir 2
print(f"{mensaje} mi nombre es: {nombre} soy de la formacion: {formacion}, tengo: {edad} años, mido:{estatura}, y peso:{peso} kg")
#actividad 1 forma
a=3
b=5
print("el resultado de la suma=",a+b,"el resultado de la resta=",a-b,"el resultado de la multipliccion=",a*b,"el resultado de la division=",a/b,"el resultado del residuo=",a%b)
#actividad 2 forma
print(f"el resultado de la suma={a+b} el resultado de la resta{a-b} el resulado de la multiplicacion={a*b} el resultado de la division{a/b} el resultado del residuo={a%b}")
"""
ejercicio pidiendo datos por teclado
"""
a=int(input("digite un valor: "))
b=int(input("digite un segundo valor: "))
print(f"el resultado de la suma={a+b} el resultado de la resta={a-b} el resulado de la multiplicacion={a*b} el resultado de la division={a/b} el resultado del residuo={a%b}")
