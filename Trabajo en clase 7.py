# agregua una palabra para buscar una letra

Palabra=input("Ingresa una palabra:  ")
Letra=input("Ingresa la letra:  ")
for Letra_consecutiva in Palabra:
    if Letra==Letra_consecutiva:
        print(f"la letra {Letra} se encontro en a palabra")
        break
    else:
        print(f"La letra {Letra} no se encontro en la palabra")
        break
