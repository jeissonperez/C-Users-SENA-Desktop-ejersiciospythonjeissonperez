# ejercicio 10:  Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:(1*2*3*4*5…).
# -----------------------------------------------------------------------------------------------
# Inicializamos el resultado en 2
numero2 = 2


# bucle sobre los números del 1 al 20
for numero in range(1, 20):
   resultado= numero2 * numero  # Multiplicamos el producto por el número por el segundo numero
   print(f"{numero} x {numero2} = {resultado}") #imprimimos la ecuacion con su resultado
   numero2+=1 #el numero va aumentando 1 para que se multiplique por el siguiente numero