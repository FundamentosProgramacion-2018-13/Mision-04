# Autor: Dvid Isaí López Jaimes      A01748363
# Programa que calcula el area y perimetro de 2 rectángulos y luego los compara para saber cual es mas grande dependiendo el área.


def calcularArea(base, altura):             # Esta función calcula el area del rectangulo
    area = base * altura
    return area


def calcularPerimetro(base, altura):            # Calcula el perímetro del rectángulo
    perimetro = (base * 2) + (altura * 2)
    return perimetro


def main():           # Aquí leemos y calculamos las funciones anteriores e imprimimos resultados
    baseRectangulo1 = int(input("Teclea la base del rectángulo 1: "))
    alturaRectangulo1 = int(input("Teclea la altura del rectángulo 1: "))
    baseRectangulo2 = int(input("Teclea la base del rectángulo 2: "))
    alturaRectangulo2 = int(input("Teclea la altura del rectángulo 2: "))

    areaRectangulo1 = calcularArea(baseRectangulo1, alturaRectangulo1)
    print("\nEl área del rectángulo 1 es: ", areaRectangulo1)
    perimetroRectangulo1 = calcularPerimetro(baseRectangulo1, alturaRectangulo1)
    print("El perímetro del rectángulo 1 es: ", perimetroRectangulo1)

    areaRectangulo2 = calcularArea(baseRectangulo2, alturaRectangulo2)
    print("\nEl área del rectangulo 2 es: ", areaRectangulo2)
    perimetroRectangulo2 = calcularPerimetro(baseRectangulo2, alturaRectangulo2)
    print("El perímetro del rectángulo 2 es: ", perimetroRectangulo2)

    if areaRectangulo2 > areaRectangulo1:
        print("\nEl rectángulo 2 tiene mayor área.")
    if areaRectangulo1 > areaRectangulo2:
        print("\nEl rectángulo 1 tiene mayor área.")
    if areaRectangulo2 == areaRectangulo1:
        print("\nAmbos rectángulos tienen la misma área.")



main()