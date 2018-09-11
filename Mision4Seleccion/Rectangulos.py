# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea las dimensiones de dos rectángulos
# y que calcule e imprima el perímetro y área de cada uno.

# Se calcula el area del primer y segundo rectángulo.
def calcularArea(ha, ba, hb, bb):
    areaRectanguloA = ha * ba
    areaRectanguloB = hb * bb
    return areaRectanguloA, areaRectanguloB


# Se calcula el perimetro del primer y segundo rectángulo.
def calcularPerimetro(ha, ba, hb, bb):
    perimetroRectanguloA = (ha * 2) + (ba * 2)
    perimetroRectanguloB = (hb * 2) + (bb * 2)
    return perimetroRectanguloA, perimetroRectanguloB

# Se compara el area del primer y del segundo rectángulo y se regresa cual es el mayor.
def calcularMayor(ha, ba, hb, bb):
    areaRectanguloA = ha * ba
    areaRectanguloB = hb * bb

    if areaRectanguloA > areaRectanguloB:
            mayor = "El primer rectángulo es nayor"
    else:
            mayor = "El segundo rectángulo es mayor"
    if areaRectanguloA == areaRectanguloB:
        mayor = "Son iguales ambos rectángulos"
    return mayor


def main():

    # Se piden la altura y base del primer rectángulo, como la del segundo rectángulo.
    alturaA = int(input("Teclee la altura del primer rectángulo: "))
    baseA = int(input("Teclee la base del primer rectángulo: "))
    alturaB = int(input("Teclee la altura del segundo rectángulo: "))
    baseB = int(input("Teclee la base del segundo rectángulo: "))

    # Se llama a la función para calcular Area, Perímetro y Mayor, respectivamente.
    area = calcularArea(alturaA,baseA,alturaB,baseB)
    perimetro = calcularPerimetro(alturaA,baseA,alturaB,baseB)
    mayor = calcularMayor(alturaA, baseA, alturaB, baseB)

    # Impresión de resultados
    print("El area del primer rectángulo es: %d unidades cuadradas y del segundo es: %d unidades cuadradas" % (area))
    print("El perímetro del primer rectángulo es: %d unidades cuadradas y del segundo es: %d unidades cuadradas" % (perimetro))
    print(mayor)

main()# Corre el programa