# Autor: Jonathan Sanabria Rocha
# Descripcion: Calcular el area y perimetro de rectangulos.


# Calcula el area del rectangulo
def calcularArea (base,altura):
    area = base * altura
    return area


# Calcula el perimetro del rectangulo
def calcularPerimetro (base,altura):
    perimetro = 2*base + 2*altura
    return perimetro


# Calcula que area es mayor o si son iguales
def calcularAreaMayor (rectangulo1,rectangulo2):
    if rectangulo1 > rectangulo2:
        return "El rectangulo 1 tiene mayor area "
    elif rectangulo1 < rectangulo2:
        return "El rectangulo 2 tiene mayor area"
    else:
        return "Las areas de los rectangulos son iguales"


#Funcion principal
def main():
    alturaRectanguloUno = int(input("Dame la altura del primer rectangulo: "))
    baseRectanguloUno = int(input("Dame la base del primer rectangulo: "))
    alturaRectanguloDos = int(input("Dame la altura del segundo rectangulo: "))
    baseRectanguloDos = int(input("Dame la base del segundo rectangulo: "))
    areaRectangulo1 = calcularArea(baseRectanguloUno,alturaRectanguloUno)
    perimetroRectangulo1 = calcularPerimetro(baseRectanguloUno,alturaRectanguloUno)
    print("El area del primer rectangulo es: ", areaRectangulo1)
    print("El perimetro del primer rectangulo es: ", perimetroRectangulo1)
    areaRectangulo2 = calcularArea(baseRectanguloDos, alturaRectanguloDos)
    perimetroRectangulo2 = calcularPerimetro(baseRectanguloDos,alturaRectanguloDos)
    print("El area del segundo rectangulo es: ", areaRectangulo2)
    print("El perimetro del segundo rectangulo es: ", perimetroRectangulo2)
    print(calcularAreaMayor(areaRectangulo1,areaRectangulo2))


#Lamar a amain
main()







