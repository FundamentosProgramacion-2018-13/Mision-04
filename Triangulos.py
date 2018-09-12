#Autor: Jose Luis Mata Lomeli
#Diferenciar cual es un triangulo Rectangulo, Isosceles o Equilaterolas medidas dadas


#Rectangulo: Cualquier triangulo con un angulo de 90 grados. senO = co/ca; hipo = raiz cuadrada de la suma de ca y co elevados al cuadrado; la hipotenusa es mayor que cualquiera de los catetos
#Isosceles: Tiene 2 lados iguales
#Equilatero: Tiene 3 lados iguales

import math
#####################################################################

def determinarRectangulo(cateto1, cateto2, hipotenusa):

    hipo = math.sqrt(cateto1**2 + cateto2**2)

    if hipo == hipotenusa:
        return("Es un triangulo rectangulo")
    else:
        return ("No es un triangulo al Cuadrado")

#############################################
def determinarIsosceles(longitud1, longitud2, longitud3):
    
    if (longitud1 == longitud2) or (longitud2 == longitud3) or (longitud1 == longitud3):
        return("Es un triangulo Isoceles")
    else:
        return("No es un Triangulo Isoceles")

#####################################################################
def determinarEquilatero(ladoA, ladoB, ladoC):

    if ladoA == ladoB and ladoB == ladoC:
        return("Es un triangulo Equilatero")
    else:
        return("No es un triangulo Equilatero")

##########################################################################
def esTriangulo(lado1, lado2, lado3):

    lado_result = lado1 + lado2

    if lado_result != lado3:
        return ("No es un triangulo")
    else:
        return ("Es triangulo")

####################################################################################
def main():

    lado1 = int(input("Escribe la magnitud del lado 1 del triangulo: "))
    lado2 = int(input("Escribe la magnitud del lado 2 del triangulo: "))
    lado3 = int(input("Escribe la magnitud del lado 3 del triangulo: "))

    tRect = determinarRectangulo(lado1, lado2, lado3)
    tIsos = determinarIsosceles(lado1, lado2, lado3)
    tEquil = determinarEquilatero(lado1, lado2, lado3)
    noTriangulo = esTriangulo(lado1, lado2, lado3)

########################################################################
    print(" ")

    print((tRect), ";" ,(tIsos), ",y" ,(tEquil))

    print(" ")

    print(noTriangulo)

main()
