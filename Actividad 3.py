#3.	Haz un programa que te diga cuál es el elemento más grande de una lista

lista = [4, 80, 23, 10, 55]

maximo = lista[0]


for elemento in lista:
    if elemento > maximo:
        maximo = elemento

print("El elemento más grande de la lista es:", maximo)
