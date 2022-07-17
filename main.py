# Leemos diccionario y escogemos palabra
def lecturaPalabra(lectura):
    palabras = []

    with open(lectura, 'r') as file:
        palabras = file.readlines()

    eleccion = random.randint(0,len(palabras)-1)
    mipalabra = palabras[eleccion]
    return mipalabra

def main():
    # Escoger palabra aleatoria
    palabra = lecturaPalabra('palabras.txt')
    print(palabra)


if __name__ == "__main__":
    import random
    main()
