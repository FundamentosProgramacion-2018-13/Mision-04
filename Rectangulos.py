#Irma Gómez Carmona, A01747743
#Calcular el area y perimetro de dos rectangulos, y comparar los resultados para ver cual es el mayor

def calcularAreaRectangulo(base, altura):  #con el producto de la base y la altura se calcula el area de un rectangulo
    area=base*altura
    return area


def obtenerMayor(area1, area2): #se comparan las areas de los triangulos para obtener el mayor
    if area1>area2:
        return "El área del rectangulo 1 es mayor a la del triangulo 2"
    if area1==area2:
        return "El area de los rectangulo es igual"
    return "El área del rectangulo 2 es ,mayor a la del triangulo 1"


def calcularPerimetro(base, altura):  #calcula el perimetro de un rectangulo sumando los dobles de la base y la altura
    perimetro=base*2+altura*2
    return perimetro


def main ():    #Obtener valores, llamar a las otras funciones y mostrar resultados
    base1 = int(input("Base del rectángulo 1: "))
    altura1 = int(input("Altura del rectángulo 1: "))
    base2 = int(input("Base del rectángulo 2: "))
    altura2 = int(input("Altura del rectángulo 2: "))

    area1=calcularAreaRectangulo(base1,altura1)
    area2=calcularAreaRectangulo(base2,altura2)
    perimetro1=calcularPerimetro(base1,altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    mayor=obtenerMayor(area1,area2)

    print("--------------------------")
    print("Area del rectangulo 1: ", area1)
    print("Area del rectangulo 2: ", area2)
    print("Periemtro del rectangulo 1: ", perimetro1)
    print("Periemtro del rectangulo 2: ", perimetro2)
    print(obtenerMayor(area1,area2))


main ()
