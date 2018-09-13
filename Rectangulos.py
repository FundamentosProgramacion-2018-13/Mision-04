# Autor: Humberto Carrillo Gómez
# Descripción: Este programa calcula el área de dos réctangulos, su perímetro y determina cual tiene mayor área.

# Calcula el area de los rectángulos
def calcularArea(ancho, alto):

    area = ancho*alto
    return area

# Calcula el perímetro de los rectángulos


def calcularPerimetro(ancho, alto):

    perimetro = 2*ancho+2*alto
    return perimetro


# Función principal: Resuelve el problema
def main():
    ancho1 = float(input("Teclea el ancho del primer rectángulo: "))
    alto1 = float(input("Teclea el alto del primer rectángulo: "))
    ancho2 = float(input("Teclea el ancho del segundo rectángulo: "))
    alto2 = float(input("Teclea el alto del segundo rectángulo: "))
    area1 = calcularArea(ancho1, alto1)
    area2 = calcularArea(ancho2, alto2)
    perimetro1 = calcularPerimetro(ancho1, alto1)
    perimetro2 = calcularPerimetro(ancho2, alto2)
    areaMayor=0
    if area1 > area2:
        areaMayor='El área del rectángulo 1 es mayor que la del rectángulo 2'
    if area1 == area2:
        areaMayor = 'Las áreas son iguales'
    if area2 > area1:
        areaMayor = 'El área del rectángulo 2 es mayor que la del rectángulo 1'

    print("El área del rectángulo uno es: %.2f" % area1, "cm2")
    print("El área del rectángulo dos es: %.2f" % area2, "cm2")
    print("El perímetro del rectángulo 1: %.2f" % perimetro1, "cm")
    print("El perímetro del rectángulo 2: %.2f" % perimetro2, "cm")
    print('--------------------------------------------------------------------------------')
    print(areaMayor)


# Llamado a la función principal
main()