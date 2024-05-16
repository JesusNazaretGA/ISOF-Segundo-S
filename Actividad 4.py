#4.	Haz un programa que te indique cual es la palabra más larga de una lista de palabras
lista_palabras = ["perro", "gato", "elefante", "jirafa", "rinoceronte",]

palabra_mas_larga = lista_palabras[0]

for palabra in lista_palabras:

    if len(palabra) > len(palabra_mas_larga):
       
        palabra_mas_larga = palabra

print("La palabra más larga de la lista es:", palabra_mas_larga)
