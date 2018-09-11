# Author: Ivan Honc Ayón     A01376466       Grupo 02
# Descripción: Este programa convierte la hora de formato 24hrs. a formato 12hrs.


# Esta función recibe las medidas y determina si es o no un triángulo rectángulo.
def esrectangulo(medidaA, medidaB, medidaC):
    rectangulo = False
    if medidaA>medidaB and medidaA>medidaC:
        hipotenusa = medidaA
        catetoA = medidaB
        catetoB = medidaC
        if catetoA ** 2 + catetoB ** 2 == hipotenusa ** 2:
            rectangulo = True
        else:
            rectangulo = False

    if medidaB>medidaA and medidaB>medidaC:
        hipotenusa = medidaB
        catetoA = medidaA
        catetoB = medidaC
        if catetoA ** 2 + catetoB ** 2 == hipotenusa ** 2:
            rectangulo = True
        else:
            rectangulo = False

    if medidaC>medidaB and medidaC>medidaA:
        hipotenusa = medidaC
        catetoA = medidaB
        catetoB = medidaA
        if catetoA ** 2 + catetoB ** 2 == hipotenusa ** 2:
            rectangulo = True
        else:
            rectangulo = False
    if medidaA==medidaB==medidaC:
        hipotenusa = medidaA
        catetoA = medidaB
        catetoB = medidaC
        if catetoA ** 2 + catetoB ** 2 == hipotenusa ** 2:
            rectangulo = True
        else:
            rectangulo = False

    return rectangulo


# Esta función recibe las medidas y determina si es o no un triángulo isósceles.
def esisosceles(medidaA, medidaB, medidaC):
    if medidaA == medidaB or medidaA == medidaC or medidaB == medidaC:
        isosceles = True
    else:
        isosceles = False

    return isosceles


# Esta función recibe las medidas y determina si es o no un triángulo equilátero.
def esequilatero(medidaA, medidaB, medidaC):
    if medidaA == medidaB == medidaC:
        equilatero = True
    else:
        equilatero = False

    return equilatero


# Esta función recibe las medidas y determina que función va a declarar el tipo de triángulo en cuestión.
def calcularTipoDeTriangulo(medidaA, medidaB, medidaC):
    if esrectangulo(medidaA, medidaB, medidaC) == True:
        tipoDeTriangulo = "Es un triángulo rectángulo."
    if esisosceles(medidaA, medidaB, medidaC) == True:
        tipoDeTriangulo = "Es un triángulo isósceles."
    if esequilatero(medidaA, medidaB, medidaC) == True:
        tipoDeTriangulo = "Es un triángulo equilatero."
    if esrectangulo(medidaA, medidaB, medidaC) == True and esisosceles(medidaA, medidaB, medidaC) == True:
        tipoDeTriangulo = "Es un triángulo isósceles y un triángulo rectángulo"
    if esrectangulo(medidaA, medidaB, medidaC) == False and esisosceles(medidaA, medidaB, medidaC) == False and esequilatero(medidaA, medidaB, medidaC) == False:
        tipoDeTriangulo = "Estos lados no corresponden a un triángulo."

    return tipoDeTriangulo


# Esta es la función principal que recibe los valores del usuario, manda a llamar a las otras funciones,
# e imprime qué tipo de triángulo forman las medidas..
def main():
    medidaA = float(input("Escribe el primer lado del triángulo: "))
    medidaB = float(input("Escribe el segundo lado del triángulo: "))
    medidaC = float(input("Escribe el tercer lado del triángulo: "))

    print(calcularTipoDeTriangulo(medidaA, medidaB, medidaC))


main()
