#Autor: Zabdiel Valentín.
#leer las dimensiones de 2 rectangulos, calcular el área-perimetro de cada uno y decir cual tiene mayor área.

def areaRectangulo(a,b):
    area=b*a
    return area


def perimetroRectangulo(a,b):
    perimetro=2*a+2*b
    return perimetro


def main():
    base1=int(input("Introdusca la base del 1° rectangulo: "))
    altura1=int(input("Introdusca la altura del 1° rectangulo: "))
    base2=int(input("Introdusca la base del 2° rectangulo: "))
    altura2=int(input("Introdusca la altura del 2° rectangulo: "))

    area1=areaRectangulo(altura1,base1)
    perimetro1=perimetroRectangulo(altura1,base1)
    area2=areaRectangulo(altura2,base2)
    perimetro2=perimetroRectangulo(altura2,base2)

    print("Área 1° rectangulo: ",area1,"perimetro: ",perimetro1)
    print("Área 2° rectangulo: ",area2,"perimetro: ",perimetro2)
    if area1==area2:
        print("Las áreas son iguales")
    if area1>area2:
        print("El 1° rectangulo tiene mayor área")
    if area1<area2:
        print("El 2° rectangulo tiene mayor área")

main()
