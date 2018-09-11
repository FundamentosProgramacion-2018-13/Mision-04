#Autor: Alejandro Torices Oliva
# Lee las dimensiones de dos rectángulos y  calcula e imprime el área y el perímetro de cada uno.

#Calcula el área del rectángulo.
def calcularArea(alto, ancho):
    area = alto * ancho
    return area


#Calcula el perímetro del rectángulo.
def calcularPerimetro(alto, ancho):
    perimetro = alto*2+ancho*2
    return perimetro


#Identifica el rectángulo con el área mayor.
def identificarAreaMayor(area1, area2):
    if area1 > area2:
        return "El primer rectángulo tiene el área mayor."
    else:
        if area2 > area1:
            return "El segundo rectángulo tiene el área mayor."
        else:
            return "Los dos rectángulos tienen áreas iguales."


#Función principal
def main():
    altoRectangulo1 = int(input("Ingrese la altura del rectángulo 1: "))
    anchoRectangulo1 = int(input("Ingrese la anchura del rectángulo 1: "))
    altoRectangulo2 = int(input("Ingrese la altura del rectángulo 2: "))
    anchoRectangulo2 = int(input("Ingrese la anchura del rectángulo 2: "))

    areaRectangulo1 = calcularArea(altoRectangulo1, anchoRectangulo1)
    areaRectangulo2 = calcularArea(altoRectangulo2, anchoRectangulo2)

    perimetroRectangulo1 = calcularPerimetro(altoRectangulo1, anchoRectangulo1)
    perimetroRectangulo2 = calcularPerimetro(altoRectangulo2, anchoRectangulo2)

    mayorArea = identificarAreaMayor(areaRectangulo1, areaRectangulo2)

    print(" ")
    print("El área del rectángulo 1 es: ", (areaRectangulo1))
    print("El perímetro del rectángulo 1 es: ", (perimetroRectangulo1))
    print(" ")
    print("El área del rectángulo 2 es: ", (areaRectangulo2))
    print("El perímetro del rectángulo 2 es: ", (perimetroRectangulo2))
    print(" ")
    print(mayorArea)


main()