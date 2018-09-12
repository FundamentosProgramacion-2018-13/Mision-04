#Autor: David Rodriguez
#Lee los lados de un triángulo y determina que tipo de trángulo es


#Determina el tipo de triángulo en abse a la longitud de sus lados
def determinarTriangulo(ladoA, ladoB, ladoC):
    if ladoA > 0 and ladoB > 0 and ladoC > 0:
        if ladoA == ladoB and ladoA == ladoC:
            triangulo = "equilátero"
        elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
            triangulo = "isósceles"
        elif (ladoA**2) + (ladoB**2) == (ladoC**2) or (ladoA**2) + (ladoC**2) == (ladoB**2) or (ladoB**2) + (ladoC**2) == (ladoA**2):
            triangulo = "rectángulo"
        else:
            triangulo = "Estos lados no corresponden a un triángulo"
    else:
        triangulo = "Estos lados no corresponden a un triángulo"

    return triangulo


#Función principal
def main():
    ladoA = int(input("Dame el primer lado: "))
    ladoB = int(input("Dame el segundo lado: "))
    ladoC = int(input("Dame el tercer lado: "))
    triangulo = determinarTriangulo(ladoA, ladoB, ladoC)
    print("Lado 1: ", ladoA)
    print("Lado 2: ", ladoB)
    print("Lado 3: ", ladoC)
    if triangulo != "Estos lados no corresponden a un triángulo":
        print("El triángulo es", triangulo)
    else:
        print(triangulo)


main()