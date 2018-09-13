#Autor: Alan Diaz Carrera
#Descripcion: Calcular el area y perimetro de dos rectangulos tras obtener sus dimensiones

def area1(base1, altura1):
    area1 = base1*altura1
    return area1

def perimetro1(base1, altura1):
    perimetro1 = (2*base1)+(2*altura1)
    return perimetro1

def area2(base2, altura2):
    area2 = base2*altura2
    return area2

def perimetro2(base2, altura2):
    perimetro2 = (2*base2)+(2*altura2)
    return perimetro2

def main():
    base1 = int(input("Base del rectangulo 1: "))
    altura1 = int(input("Altura del rectangulo 1: "))
    base2 = int(input("Base del rectangulo 2: "))
    altura2 = int(input("Altura del rectangulo 2: "))
    perimetroP = perimetro1(base1, altura1)
    areaP = area1(base1, altura1)
    perimetroS = perimetro2(base2, altura2)
    areaS = area2(base2, altura2)
    print("Area del rectangulo 1: ",areaP)
    print("Perimetro del rectangulo 1: ", perimetroP)
    print("Area del rectangulo 2: ", areaS)
    print("Perimetro del rectangulo 2: ", perimetroS)
    if areaP < areaS:
        print("El area del rectangulo 2 es mayor")
    if areaS < areaP:
        print("El area del rectangulo 1 es mayor")
    if areaP == areaS:
        print("Los 2 rectangulos tienen el mismo area")


main()
