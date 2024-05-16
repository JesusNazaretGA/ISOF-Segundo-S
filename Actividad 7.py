#7.	Haz un programa dónde a partir de 1 número aleatorio del uno al 10 y otro 
#ingresado por el usuario, dónde si son iguales le diga que será acreedor a un cupón.

import random

def generar_numero_aleatorio():
    return random.randint(1, 10)
def main():
    numero_aleatorio = generar_numero_aleatorio()
    while True:
        try:
            numero_usuario = int(input("Ingresa un número del 1 al 10: "))
            if numero_usuario < 1 or numero_usuario > 10:
                print("Por favor, ingresa un número válido del 1 al 10.")
                continue
            else:
                break
        except ValueError:
            print("Por favor, ingresa un número entero del 1 al 10.")
    if numero_usuario == numero_aleatorio:
        print("¡Felicidades! Eres acreedor a un cupón.")
    else:
        print("Lo siento, los números no coinciden. Mejor suerte la próxima vez.")

if __name__ == "__main__":
    main()