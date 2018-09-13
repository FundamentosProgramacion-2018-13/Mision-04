#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que calcula el perímetro y área de dos rectángulos, y determina que área es más grande o si son iguales.


#Función que calcula el área de un rectángulo.
def calcularAreaRectangulo(base, altura):
    area = base * altura
    return area


#Función que calcula el perímetro de un rectángulo.
def calcularPerimetroRectangulo(base, altura):
    perimetro = 2 * base + 2 * altura
    return perimetro


#Función que determina cuál de las dos áreas de los rectángulos es más grande.
def esMayor(area1, area2):

    if area1 > area2:
        return "El área del primer rectángulo es más grande."
    elif area1 < area2:
        return "El área del segundo rectángulo es más grande."
    else:
        return "Las áreas de los rectángulos son iguales."


#Función principal. Lee datos e imprime resultados.
def main():
    baseRectanguloA = int(input("Base del primer rectángulo: "))
    alturaRectanguloA = int(input("Altura del primer rectángulo: "))
    baseRectanguloB = int(input("Base del segundo rectángulo: "))
    alturaRectanguloB = int(input("Altura del segundo rectángulo: "))

    areaA = calcularAreaRectangulo(baseRectanguloA, alturaRectanguloA)
    areaB = calcularAreaRectangulo(baseRectanguloB, alturaRectanguloB)
    perimetroA = calcularPerimetroRectangulo(baseRectanguloA, alturaRectanguloA)
    perimetroB = calcularPerimetroRectangulo(baseRectanguloB, alturaRectanguloB)
    areaMayor = esMayor(areaA, areaB)

    print()
    print("El área del primer rectángulo es: %d" % areaA)
    print("El perímetro del primer rectángulo es: %d" % perimetroA)
    print()
    print("El área del segundo rectángulo es: %d " % areaB)
    print("El perímetro del segundo rectángulo es: %d " % perimetroB)
    print()
    print(areaMayor)


#Llamar a la función principal
main()