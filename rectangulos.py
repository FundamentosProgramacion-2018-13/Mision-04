#Autor: Jesús Emmanuel Alcalá Nava
#Descripción: este programa calcula el área y perímetro de los rectangulos a partir de la info dada por el usuario y determina cuál es mayor


def area1(base1, altura1): #calcula el área de el rectángulo 1
    area1 = base1*altura1
    return area1


def perimetro1(base1, altura1): #calcula el perímetro del rectángulo 1
    perimetro1 = (2*base1)+(2*altura1)
    return perimetro1


def area2(base2, altura2): #calcula el área de el rectángulo 2
    area2 = base2*altura2
    return area2


def perimetro2(base2, altura2): #calcula el perímetro del rectángulo 1
    perimetro2 = (2*base2)+(2*altura2)
    return perimetro2


def main():
    base1 = int(input("Cuál es la base del rectángulo 1? "))
    altura1 = int(input("Cuál es la altura del rectángulo 1? "))
    base2 = int(input("Cuál es la base del rectángulo 2? "))
    altura2 = int(input("Cuál es la altura del rectángulo 2? "))
    perimetroG = perimetro1(base1, altura1)
    areaG = area1(base1, altura1)
    perimetroC = perimetro2(base2, altura2)
    areaC = area2(base2, altura2)
    print("Área del rectángulo 1: ",areaG)
    print("Perímetro del rectángulo 1: ", perimetroG)
    print("Área del rectángulo 2: ", areaG)
    print("Perímetro del rectángulo 2: ", perimetroG)
    if areaG < areaC:
        print("El área del rectángulo 2 es mayor")
    if areaC < areaG:
        print("El área del rectángulo 1 es mayor")
    if areaC == areaG:
        print("Los 2 rectángulos tienen la misma área")
main()