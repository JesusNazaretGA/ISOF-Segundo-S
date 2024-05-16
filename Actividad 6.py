#6.	Haz un programa dónde hagas una resta y te diga si el resultado es un numero 
#positivo o negativo.

def resta_y_signo(numero1, numero2):
    resultado = numero1 - numero2
    if resultado > 0:
        print("El resultado de la resta es positivo.")
    elif resultado < 0:
        print("El resultado de la resta es negativo.")
    else:
        print("El resultado de la resta es cero.")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

resta_y_signo(numero1, numero2)