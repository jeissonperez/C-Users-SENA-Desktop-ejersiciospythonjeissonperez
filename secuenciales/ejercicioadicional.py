#Ejercicio adicional
# Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las
# siguientes apreciaciones:
# Actividades en clase equivalen a un porcentaje de 30%
# Proyecto final 50%
# Evaluaciones parciales 20%
nombre=(input("Ingrese el nombre del estudiante: "))
calificacion_actividades = float(input("Ingrese la calificación promedio de las actividades en clase (0-100): "))
calificacion_proyecto = float(input("Ingrese la calificación del proyecto final (0-100): "))
calificacion_evaluaciones = float(input("Ingrese la calificación promedio de las evaluaciones parciales (0-100): "))

peso_actividades=0.30
peso_proyecto=0.50
peso_evaluaciones=0.20

nota_final = (calificacion_actividades * peso_actividades) + (calificacion_proyecto * peso_proyecto) + (calificacion_evaluaciones * peso_evaluaciones)

print(f"La nota final de algoritmia del estudiante {nombre} es: {nota_final:.2f}")