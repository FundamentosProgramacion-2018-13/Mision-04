# Oscar Alejandro Torres Maya, A01377686
# Calcular el perímetro y área de dos rectángulos y aparte indicar que área es mayor

# Función para calcular las áreas
def calcularArea(largo, ancho):
    area = largo * ancho
    return area


# Función para calcular los perímetros
def calcularPerimetro(largo,ancho):
    perimetro = (2*largo) + (2*ancho)
    return perimetro


# Función principal
def main():
    largo1 = float(input("Escribe el largo del primer rectángulo: "))
    ancho1 = float(input("Escribe el ancho del primer rectángulo: "))
    largo2 = float(input("Escribe el largo del segundo rectángulo: "))
    ancho2 = float(input("Escribe el ancho del segundo rectángulo: "))

    area1 = calcularArea(largo1,ancho1)
    area2 = calcularArea(largo2,ancho2)
    perimetro1 = calcularPerimetro(largo1,ancho1)
    perimetro2 = calcularPerimetro(largo2,ancho2)

    print("El perímetro del primer rectángulo es: ", perimetro1)
    print("El perímetro del segundo rectángulo es: ", perimetro2)
    print("El área del primer rectángulo es: ", area1)
    print("El área del segundo rectángulo es: ", area2)

    if area1 > area2:
        print("El área del primer rectángulo es mayor")
    else:
        print("El área del segundo rectángulo es mayor")

    if area1 == area2:
        print("El área de los dos rectángulos es igual")

# Llamada de función principal
main()