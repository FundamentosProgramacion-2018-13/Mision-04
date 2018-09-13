#Jocelyn López Ortíz A01377451
#Calcular el área y perímetro de dos rectángulos


def calcularArea(a, b): #Calcular el área de un rectángulo
    area = a*b
    return area


def calcularPerimetro(a, b):  #Calcular el perímetro de un rectángulo
    perimetro = 2*a + 2*b
    return perimetro


def main():
    rectangulo1lado1 = int(input("Teclea el lado 1 del rectángulo 1: "))
    rectangulo1lado2 = int(input("Teclea el lado 2 del rectángulo 1: "))
    rectangulo2lado1 = int(input("Teclea el lado 1 del rectángulo 2: "))
    rectangulo2lado2 = int(input("Teclea el lado 2 del rectángulo 2: "))

    area1 = calcularArea(rectangulo1lado1, rectangulo1lado2)
    perimetro1 = calcularPerimetro(rectangulo1lado1, rectangulo1lado2)
    area2 = calcularArea(rectangulo2lado1, rectangulo2lado2)
    perimetro2 = calcularPerimetro(rectangulo2lado1, rectangulo2lado2)

    print()
    print("Área del rectángulo 1: ", area1)
    print("Perímetro del rectangulo 1: ", perimetro1)
    print()
    print("Área del rectángulo 2: ", area2)
    print("Perímetro del rectangulo 2: ", perimetro2)
    print()

    if area1>area2:
        print("El rectángulo con área mayor es el rectángulo 1")
    if area1<area2:
        print("El rectángulo con área mayor es el rectángulo 2")
    if area1 == area2:
        print("Los rectángulos tienen la misma área")


main()