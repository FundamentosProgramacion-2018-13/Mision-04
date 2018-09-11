#Autor: Claudio Mayoral García
#Descripción es un programa que calcula el area y el perímetro de dos rectángulos pidiendo las dimensiones


#Calcula el área del rectángulo uno con una función
def calcularArea1(base1, altura1):
    area1 = base1 * altura1
    return area1


#Calcula el área del rectángulo dos con una función
def calcularArea2(base2, altura2):
    area2 = base2 * altura2
    return area2


#Calcula el perímetro del rectángulo uno con una función
def calcularPerimetro1(base1, altura1):
    perimetro1 = 2 * base1 + 2 * altura1
    return perimetro1


#Calcula el perímetro del rectángulo dos con una función
def calcularPerimetro2(base2, altura2):
    perimetro2 = 2 * base2 + 2 * altura2
    return perimetro2


#Calcula cual rectángulo tiene mayor área o si ambas áreas son iguales
def calcularMayorArea(area1, area2):
    if area1 < area2:
        return "El rectángulo 2 tiene más superficie"
    elif area2 < area1:
        return "El rectángulo 1 tiene más superficie"
    elif area1 == area2:
        return "Los dos rectángulos tienen la misma superficie"


#Función Principal
def main():
    base1 = float(input("Escribe la base del rectángulo 1: "))
    altura1 = float(input("Escribe la altura del rectángulo 1: "))
    base2 = float(input("Escribe la base del rectángulo 2: "))
    altura2 = float(input("Escribe altura del rectángulo 2: "))
    area1 = calcularArea1(base1, altura1)
    area2 = calcularArea2(base2, altura2)
    perimetro1= calcularPerimetro1(base1, altura1)
    perimetro2 = calcularPerimetro2(base2, altura2)
    print("-----------------------------------------------------------")
    print("El área del rectángulo 1 es de: %.2f cm2" % area1)
    print("EL perímetro del rectángulo 1 es de: %.2f cm" % perimetro1)
    print("-----------------------------------------------------------")
    print("El área del rectángulo 2 es de: %.2f cm2" % area2)
    print("EL perímetro del rectángulo 2 es de: %.2f cm" % perimetro2)
    print("-----------------------------------------------------------")
    print(calcularMayorArea(area1, area2))


#llama a la función principal
main()
