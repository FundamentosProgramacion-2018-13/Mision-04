#Joshua Sánchez Martínez A01274269
#Este programa lee dimensiones de dos rectangulos, calcula el perimetro y area, además decir cual tiene mayor area o si son iguales


#Calcula el area del primer rectangulo
def area1 (ancho,largo):
    area =  ancho*largo
    return area


#Calcula el area del segundo rectangulo
def area2 (ancho,largo):
    area = ancho*largo
    return area


#Calcula el primer perimetro
def perimetro1 (ancho,largo):
    perimetro = ancho*2 + largo*2
    return perimetro


#Calcula el segundo perimetro
def perimetro2 (ancho,largo):
    perimetro = ancho*2 + largo*2
    return perimetro


#Funcion principal
def main ():
    anchoRectangulo1 = int(input("Ancho del rectangulo 1: "))
    largoRectangulo1 = int(input("Largo del rectangulo 1: "))

    anchoRectangulo2 = int(input("Ancho del rectangulo 2: "))
    largoRectangulo2 = int(input("Largo del rectangulo 2: "))

    areaRectangulo1 = area1(anchoRectangulo1,largoRectangulo1)
    areaRectangulo2 = area2(anchoRectangulo2,largoRectangulo2)

    perimetroRectangulo1 = perimetro1(anchoRectangulo1,largoRectangulo1)
    perimetroRectangulo2 = perimetro2(anchoRectangulo2,largoRectangulo2)

    print("El perimetro del primer rectangulo es: ", perimetroRectangulo1)
    print("El perimetro del segundo rectangulo es: ", perimetroRectangulo2)

    print("El area del primer rectangulo es: ", areaRectangulo1)
    print("El area del segundo rectangulo es: ", areaRectangulo2)

    if areaRectangulo1 > areaRectangulo2:
        print("El area del primer rectangulo es mayor")
    else:
        if areaRectangulo1 < areaRectangulo2:
            print("El area del segundo rectangulo es mayor")
        else:
            print("Las areas son iguales")


#Llamar a la función main
main()