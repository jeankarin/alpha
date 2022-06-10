def lecturaPalabra(lectura):
    palabras = []
    fichero = open(lectura,'r')
    lineas = csv.reader(fichero)
    for line in lineas:
        palabras.append(line)

    choice = random.randint(0,len(palabras)-1)

def main():
    # Escoger palabra aleatoria
    palabra = lecturaPalabra('palabras.txt')


if __name__ == "__main__":
    import csv
    import random
    main()
