# Autor: Rubén Villalpando Bremont
# Este programa lee las dimensiones de dos rectángulos, te da el perímetro y área de cada uno y te dice el
# que tiene mayor área.


# Calcula cuál área de los 2 rectángulos es mayor
def calcularAreaMayor(rectanguloUno, rectanguloDos):
    if rectanguloUno > rectanguloDos:
        return "El primer rectángulo tiene mayor área"
    elif rectanguloUno < rectanguloDos:
        return "El segundo rectángulo tiene mayor área"
    return "Los dos rectángulos tienen la misma área"


# Calcula el perimetro de un rectángulo
def calcularPerimetro(base, altura):
    perimetroRectangulo = 2*base + 2*altura
    return perimetroRectangulo


# Calcula el área de un rectángulo
def calcularArea(base, altura):
    areaRectangulo = base * altura
    return areaRectangulo


# Función principal
def main():
    baseRectanguloUno = int(input("Escribe la base del primer rectángulo: "))
    alturaRectanguloUno = int(input("Escribe la altura del primer rectángulo: "))
    baseRectanguloDos = int(input("Escribe la base del segundo rectángulo: "))
    alturaRectanguloDos = int(input("Escribe la altura del segundo rectángulo: "))
    areaRectanguloUno = calcularArea(baseRectanguloUno, alturaRectanguloUno)
    areaRectanguloDos = calcularArea(baseRectanguloDos, alturaRectanguloDos)
    perimetroRectanguloUno = calcularPerimetro(baseRectanguloUno, alturaRectanguloUno)
    perimetroRectanguloDos = calcularPerimetro(baseRectanguloDos, alturaRectanguloDos)
    print("El área del primer rectángulo es: ", areaRectanguloUno)
    print("El perímetro del segundo rectánguloes: ", perimetroRectanguloUno)
    print("El área del segundo rectángulo es: ", areaRectanguloDos)
    print("El perímetro del segundo rectángulo es: ", perimetroRectanguloDos)
    print(calcularAreaMayor(areaRectanguloUno, areaRectanguloDos))

# Llamar a main
main()