# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que calcula las dimensiones de dos rectángulos y que calcula e imprime el área y perímetro.


# La siguiente función calcula el área de los rectángulos.
def calcularArea(ancho, largo):
    area = ancho * largo
    return area


# La siguiente función calcula el perímetro de los rectángulos.
def calcularPerimetro(ancho, largo):
    perimetro = ancho * 2 + largo * 2
    return perimetro


# La siguiente función se encarga de comparar las áreas de los rectángulos y determinar cuál es la mayor o si son
# iguales.
def calcularMayor(areaDelRectangulo1, areaDelRectangulo2):
    if areaDelRectangulo1 == areaDelRectangulo2:
        return "Ambas áreas son iguales"
    else:
        if areaDelRectangulo1 > areaDelRectangulo2:
            return "El área del rectángulo 1 es mayor al área del rectángulo 2"
        else:
            return "El área del rectángulo 2 es mayor al área del rectángulo 1"



# La función principal se encarga de leer los datos e imprimir el resultado final.
def main():
    anchoDelRectangulo1 = float(input("Teclea el ancho del primer rectangulo: "))
    largoDelRectangulo1 = float(input("Teclea el largo del primer rectangulo: "))
    anchoDelRectangulo2 = float(input("Teclea el ancho del segundo rectangulo: "))
    largoDelRectangulo2 = float(input("Teclea el largo del segundo rectangulo: "))

    areaDelRectangulo1 = calcularArea(anchoDelRectangulo1, largoDelRectangulo1)
    areaDelRectangulo2 = calcularArea(anchoDelRectangulo2, largoDelRectangulo2)

    perimetroDelRectangulo1 = calcularPerimetro(anchoDelRectangulo1, largoDelRectangulo1)
    perimetroDelRectangulo2 = calcularPerimetro(anchoDelRectangulo2, largoDelRectangulo2)

    mayor = calcularMayor(areaDelRectangulo1, areaDelRectangulo2)

    print("""

    Area del primer rectangulo: %d
    Perimetro del primer rectangulo: %d
    Area del primer rectangulo: %d 
    Perimetro del primer rectangulo: %d

    %s
    """ % (areaDelRectangulo1, perimetroDelRectangulo1, areaDelRectangulo2, perimetroDelRectangulo2, mayor))

# Llamada a la función main.
main()


