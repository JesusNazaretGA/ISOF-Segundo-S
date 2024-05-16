# actividad en la que se realizaran intentos para adivinar cierto numero
# que te arrojaran aleatoriamente

from random import Random


intentos_realizados=0
print("Tienes 5 intentos para adivinar el numero ")
Numero=Random.randint(1,10)
while intentos_realizados<=5:
    Numero_ingresado=int(input("Ingresa un numero entre el 1-10  "))
    if Numero_ingresado>Numero:
        print("El numero es mayor")
    elif Numero_ingresado<Numero:
        print("El numero es meron ")
    else:
        print("Numero encontrado ")
        break
intentos_realizados=intentos_realizados+1