#Autor: Luis Ricardo Chagala Cervantes.
#Con las medidas ingresadas determinar Área y Perimetro de ambos Rectongulos y determinar que Rectangulo tiene mayor Área.

def areaRectangulo1(a1, b1):
    area1 = a1 * b1
    return area1


def perimetroRectangulo1(a1, b1):
    perimetro1 = 2 * a1 + 2 * b1
    return perimetro1


def areaRectangulo2(a2, b2):
    area2 = a2 * b2
    return area2


def perimetroRectangulo2(a2, b2):
    perimetro2 = 2 * a2 + 2 * b2
    return perimetro2


def imprimir(area1, area2, perimetro1, perimetro2):
    print("Área del primer rectangulo: ", area1, "Perimetro: ", perimetro1)
    print("Área del segundo rectangulo: ", area2, "Perimetro: ", perimetro2)
    if area1 == area2:
        print("Las Áreas son iguales")
    if area1 > area2:
        print("El primer rectangulo tiene una mayor Área")
    if area1 < area2:
        print("El segundo rectangulo tiene una mayor Área")


def main():
    base1 = int(input("Base del primer rectangulo: "))
    altura1 = int(input("Altura del primer rectangulo: "))
    base2 = int(input("Base del segundo rectangulo: "))
    altura2 = int(input("Altura del segundo rectangulo: "))

    area1 = areaRectangulo1(altura1, base1)
    perimetro1 = perimetroRectangulo1(altura1, base1)
    area2 = areaRectangulo2(altura2, base2)
    perimetro2 = perimetroRectangulo2(altura2, base2)
    imprimir(area1, area2, perimetro1, perimetro2)


main()
