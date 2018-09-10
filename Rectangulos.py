# Autor: Silvia Ferman Muñoz
# Programa que lee las dimensiones de dos rectangulos e imprime sus perimentos y areas
# Tecnica Top-Down


# Calcular el área de los rectángulos utlizando su base y altura
def calcularArea(b,h):
    return b * h


# Calculr el perímetro de los rectángulos utlizando su base y altura
def calcularPerimetro(b,h):
    return (2 * b) + (2 * h)


# Calcular que rectangulo tiene mayor área
def calcularAreaMayor(A1, A2):
     if A1 == A2:
         return "Las áreas de los rectangulos son iguales"
     else:
         if A1 > A2:
             return "El primer rectángulo tiene mayor área"
         else:
             return "El segundo rectangulo tiene mayor área"


# Función principal
def main():
     baseRectanguloUno = int(input("La base del primer rectángulo es: "))
     alturaRectanguloUno = int(input("La altura del primer rectángulo es: "))
     baseRectanguloDos = int(input("La base del segundo rectángulo es: "))
     alturaRectanguloDos = int(input("La altura del segundo rectángulo es: "))

     areaRectanguloUno = calcularArea(baseRectanguloUno, alturaRectanguloUno)
     areaRectanguloDos = calcularArea(baseRectanguloDos, alturaRectanguloDos)

     print("El área del rectangulo uno es: %d" % areaRectanguloUno)
     print("El perímetro del rectángulo uno es: %d" % calcularPerimetro(baseRectanguloUno, alturaRectanguloUno))
     print("El área del rectángulo dos es: %d" % areaRectanguloDos)
     print("El perímetro del rectángulo dos es: %d" % calcularPerimetro(baseRectanguloDos, alturaRectanguloDos))
     print("%s" % (calcularAreaMayor(areaRectanguloUno, areaRectanguloDos)))


# Llama a la función principal
main()