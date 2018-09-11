# Author: Ivan Honc Ayón     A01376466       Grupo 02
# Descripción: Este programa calcula el área y el perímetro de dos rectángulos
# y determina cual tiene mayor área, o si los dos son iguales.


# Esta función recibe el lado y la altura de un rectángulo y calcula su perímetro, regresa el perímetro.
def calcularPerimetro(ladoTriangulo, alturaTriangulo):
    perimetro = ladoTriangulo*2 + alturaTriangulo*2

    return perimetro


# Esta función recibe el lado y la altura de un rectángulo y calcula su área, regresa el área.
def calcularArea(ladoTriangulo, alturaTriangulo):
    area = ladoTriangulo*alturaTriangulo

    return area


# Esta función recibe el área de dos rectángulos y las compara, regresa una cadena con el área
# que sea mayor, o, en su defecto, declarando que las áreas son iguales.
def calcularAreaMayor(areaA, areaB):
    if areaA>areaB:
        areaMayor = "El área del rectángulo A es mayor"
    if areaB>areaA:
        areaMayor = "El área del rectángulo B es mayor"
    if areaA==areaB:
        areaMayor = "Las áreas de los rectángulos son iguales"

    return areaMayor


# Esta es la función principal que recibe la entrada del usuario, manda a llamar a las funciones
# e imprime los resultados.
def main():
    ladoRectanguloA = float(input("Teclea el lado del rectángulo A: "))
    alturaRectanguloA = float(input("Teclea la altura del rectángulo A: "))
    ladoRectanguloB = float(input("Teclea el lado del rectángulo B: "))
    alturaRectanguloB = float(input("Teclea la altura del rectángulo B: "))
    areaA = calcularArea(ladoRectanguloA, alturaRectanguloA)
    areaB = calcularArea(ladoRectanguloB, alturaRectanguloB)
    areaMayor = (calcularAreaMayor(areaA, areaB))

    print ("""
El perímetro del rectángulo A es: %.2fm
El área del rectángulo A es: %.2fm^2

El perímetro del rectángulo B es: %.2fm
El área del rectángulo B es %.2fm^2

%s""" % (calcularPerimetro(ladoRectanguloA, alturaRectanguloA), calcularArea(ladoRectanguloA, alturaRectanguloA),
         calcularPerimetro(ladoRectanguloB, alturaRectanguloB), calcularArea(ladoRectanguloB, alturaRectanguloB),
         areaMayor))


main()
