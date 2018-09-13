#Autor: Alberto Contreras Torres
#Leé las dimensiones de los rectángulos y calcula e imprime el perimetro de cada uno. Indica cual tiene mayor área o si son iguales.


#recibe baseMayor1 y baseMenor1 y calcula el area del rectangulo 1
def calcularArea1(baseMayor1, baseMenor1):
    area1 = baseMayor1 * baseMenor1
    return area1


#recibe baseMayor1 y baseMenor1 y alcula el perimetro del rectangulo 1
def calcularPerimetro1(baseMayor1, baseMenor1):
    perimetro1 = baseMayor1 * 2 + baseMenor1 * 2
    return perimetro1


#recibe baseMayor2 y baseMenor2 y calcula el area del rectangulo 2
def calcularArea2(baseMayor2, baseMenor2):
    area2 = baseMayor2 * baseMenor2
    return area2


#recibe baseMayor2 y baseMenor2 y calcula el perimetro del rectangulo 2
def calcularPerimetro2(baseMayor2, baseMenor2):
    perimetro2 = baseMayor2 * 2 + baseMenor2 * 2
    return perimetro2


# Imprime area1, perimetro1, area2, perimetro2
def imprimir(area1, perimetro1, area2, perimetro2):
    print("Area de Rectángulo 1: ", area1)
    print("Perimetro de Rectángulo 1: ", perimetro1)
    print("Area de Rectángulo 2: ", area2)
    print("Perimetro de Rectángulo 2: ", perimetro2)


# Función principal
def main():
    baseMayor1 = int(input("Teclea Base Mayor del rectangulo 1: "))
    baseMenor1 = int(input("Teclea Base Menor del rectangulo 1: "))
    baseMayor2 = int(input("Teclea Base Mayor del rectangulo 2: "))
    baseMenor2 = int(input("Teclea Base Menor del rectangulo 2: "))
    area1= calcularArea1(baseMayor1, baseMenor1)
    perimetro1 =calcularPerimetro1(baseMayor1, baseMenor1)
    area2 = calcularArea2(baseMayor2, baseMenor2)
    perimetro2 = calcularPerimetro2(baseMayor2, baseMenor2)
    imprimir(area1, perimetro1, area2, perimetro2)
    if area1 > area2:
        print("Rectangulo 1 tiene mayor área")
    elif area1 < area2:
        print("Rectangulo 2 tiene mayor área")
    else:
        print("Ambos tienen el mismo área")
main()
