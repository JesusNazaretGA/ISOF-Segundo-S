#8.	Haz un programa dónde el usuario pueda solicitar ver una película a partir de una lista
#dada por el sistema, dónde considere su edad, 2 películas deberán ser para mayores de 18 años.

class Pelicula:
    def __init__(self, titulo, clasificacion):
        self.titulo = titulo
        self.clasificacion = clasificacion
peliculas = [
    Pelicula("El Señor de los Anillos", "PG-13"),
    Pelicula("La La Land", "PG-13"),
    Pelicula("The Godfather", "R"),
    Pelicula("Pulp Fiction", "R"),
    Pelicula("Deadpool", "R"),
    Pelicula("The Hangover", "R"),
]
def mostrar_peliculas(edad):
    print("Peliculas recomendadas:")
    for pelicula in peliculas:
        if edad >= 18 or pelicula.clasificacion != "R":
            print(pelicula.titulo)
def main():
    print("Bienvenido al sistema de recomendación de películas.")
    while True:
        try:
            edad = int(input("Por favor, introduce tu edad: "))
            if edad < 0:
                print("La edad no puede ser un número negativo. Intenta de nuevo.")
                continue
            mostrar_peliculas(edad)
            break
        except ValueError:
            print("Por favor, introduce un número entero válido.")

if __name__ == "__main__":
    main()