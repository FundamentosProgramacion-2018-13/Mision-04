# Autor: Zoe Caballero Dominguez
#El programa determina qué tipo de triángulo se forma con los tres lados proporcionados por el usuario.

# La función determina el tipo de triángulo es: equilátero, rectángulo o isóceles
def determinarTriangulo (ladoTrianguloA, ladoTrianguloB, ladoTrianguloC):
    if ladoTrianguloA == ladoTrianguloB and ladoTrianguloA == ladoTrianguloC:
        return "Equilatero"
    elif (ladoTrianguloA**2 == ladoTrianguloB**2 + ladoTrianguloC**2) or (ladoTrianguloB**2 == ladoTrianguloA**2 + ladoTrianguloC**2) or (ladoTrianguloC**2 == ladoTrianguloA**2 + ladoTrianguloB**2):
        return "Rectángulo"
    elif (ladoTrianguloA == ladoTrianguloB and ladoTrianguloA != ladoTrianguloC) or (ladoTrianguloB == ladoTrianguloC and ladoTrianguloB != ladoTrianguloA) or (ladoTrianguloC == ladoTrianguloA and ladoTrianguloC != ladoTrianguloB):
        return "Isóceles"
    else:
        return "El triángulo no existe"


# Función principal
def main():
    ladoTrianguloA = int(input("Escriba el primer lado del triángulo: "))
    ladoTrianguloB = int (input("Escriba el segundo lado del triángulo: "))
    ladoTrianguloC = int (input("Escriba el tercer lado del triángulo: "))

    if ladoTrianguloC > 0 and ladoTrianguloA > 0 and ladoTrianguloB > 0:
        print("El triángulo es: ", determinarTriangulo(ladoTrianguloA, ladoTrianguloB, ladoTrianguloC))
    else:
        print ("El triángulo no existe")


#Llamar a la función
main()
