def lecturaPalabra(lectura):
    palabras = []
    fichero = open(lectura,'r')
    lineas = csv.reader(fichero)
    for line in lineas:
        palabras.append(line)

    eleccion = random.randint(0,len(palabras)-1)
    mipalabra = palabras[eleccion]
    return mipalabra

def main():
    # Escoger palabra aleatoria
    palabra = lecturaPalabra('palabras.txt')
    print(palabra)


if __name__ == "__main__":
    import csv
    import random
    main()
