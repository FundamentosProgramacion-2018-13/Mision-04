# Autor: Erick David Ramírez Martínez, A01748155
"""Descripción, programa que lee los 3 lados de un triángulo y con base a ello,
descubre si el triángulo existe y lo clasifica según corresponda"""


def calcularLaExistencia(lado1, lado2, lado3):
    if lado1+lado2 > lado3 and lado1+lado3 > lado2 and lado2+lado3 > lado3:
        return "Existe"
    else:
        return "No existe"


def clasificarTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Triángulo equilátero"
    else:
        if (lado1**2 + lado2**2)**0.5 == lado3 or (lado1**2 + lado3**2)**0.5 == lado2 or (lado2**2 + lado3**2)**0.5 == lado1:
            return "Triángulo rectángulo"
        else:
            if lado1 == lado2 and lado2 != lado3:
                return "Triángulo isósceles"
            else:
                if lado3 == lado2 and lado2 != lado1:
                    return "Triángulo isósceles"
                else:
                    if lado1 == lado3 and lado3 != lado2:
                        return "Triángulo isósceles"
                    else:
                        return "Triángulo escaleno"


def main():
    lado1= int(input("Ingrese la medida del primer lado: "))
    lado2 = int(input("Ingrese la medida del segundo lado: "))
    lado3 = int(input("Ingrese la medida del tercer lado: "))

    existencia = calcularLaExistencia(lado1,lado2,lado3)
    clase = clasificarTriangulo(lado1,lado2,lado3)

    print("El triangulo: ",existencia)
    if existencia == "Existe":
        print("Es un: ",clase)


main()