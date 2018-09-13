# Autor: Erick David Ramírez Martínez, A01748155
"""Descripción, programa que lee las dimensiones de 2 rectángulos, calcula su área, perímetro
 y compara sus áreas para indicar cual es mayor"""


def calcularAreaRectangulo(x, y):
    area = x * y
    return area


def calcularPerimetroRectangulo(x, y):
    perimetro = 2*x + 2*y
    return perimetro


def calcularAreaMayor(areaRectangulo1, areaRectangulo2):
    if areaRectangulo1 > areaRectangulo2:
        return "Rectángulo 1"
    else:
        if areaRectangulo1 < areaRectangulo2:
            return "Rectángulo 2"
        else:
            return "Ninguno"


def main():
    baseRectangulo1 = int(input("Base del primer rectángulo: "))
    alturaRectangulo1 = int(input("Altura del primer rectángulo: "))
    baseRectangulo2 = int(input("Base del segundo rectángulo: "))
    alturaRectangulo2 = int(input("Altura del segundo rectángulo: "))
    print("")

    areaRectangulo1 = calcularAreaRectangulo(baseRectangulo1,alturaRectangulo1)
    areaRectangulo2 = calcularAreaRectangulo(baseRectangulo2,alturaRectangulo2)

    perimetroRectangulo1 = calcularPerimetroRectangulo(baseRectangulo1,alturaRectangulo1)
    perimetroRectangulo2 = calcularPerimetroRectangulo(baseRectangulo2,alturaRectangulo2)

    areaMayor = calcularAreaMayor(areaRectangulo1,areaRectangulo2)

    print("El área del rectángulo 1 es: ", areaRectangulo1)
    print("El área del rectángulo 2 es: ", areaRectangulo2)
    print("El perímetro del rectántulo 1 es: ", perimetroRectangulo1)
    print("El perímetro del rectántulo 2 es: ", perimetroRectangulo2)
    print("El rectángulo mayor área es: ", areaMayor)
    if areaRectangulo2 == areaRectangulo1:
        print("El área de los rectángulos es igual")


main()