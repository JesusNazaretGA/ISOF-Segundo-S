#10.	Haz un programa que ayude a calcular la calificación de un examen, dónde el usuario 
#deberá ingresar, el total de preguntas, la cantidad de preguntas con respuestas correctas 
#y la cantidad con respuestas incorrectas

def calcular_calificacion(total_preguntas, preguntas_correctas, preguntas_incorrectas):
    puntaje = (preguntas_correctas / total_preguntas) * 100
 
    if puntaje >= 70:
        calificacion = "Aprobado"
    else:
        calificacion = "No aprobado"
    return puntaje, calificacion

def main():
    total_preguntas = int(input("Ingrese el total de preguntas del examen: "))
    preguntas_correctas = int(input("Ingrese la cantidad de preguntas correctas: "))
    preguntas_incorrectas = int(input("Ingrese la cantidad de preguntas incorrectas: "))

    puntaje, calificacion = calcular_calificacion(total_preguntas, preguntas_correctas, preguntas_incorrectas)

    print("\nResultados del examen:")
    print("Total de preguntas:", total_preguntas)
    print("Preguntas correctas:", preguntas_correctas)
    print("Preguntas incorrectas:", preguntas_incorrectas)
    print("Puntaje obtenido: {:.2f}%".format(puntaje))
    print("Calificación:", calificacion)

if __name__ == "__main__":
    main()