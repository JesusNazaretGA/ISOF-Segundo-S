#2.	Haz un programa que te calcule el promedio de una lista de calificaciones
calificaciones = []
cantidad = int(input("Ingrese la cantidad de calificaciones: "))

for i in range(cantidad):
        calificacion = int(input(f"Ingrese la calificación {i+1}: "))
        calificaciones.append(calificacion)

if len(calificaciones) > 0:
        promedio = sum(calificaciones) / len(calificaciones)
        print("El promedio de las calificaciones es:", promedio)
        