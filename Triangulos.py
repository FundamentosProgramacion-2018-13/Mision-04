#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que determina si un triángulo existe. Si existe, determina si es un triángulo rectángulo, isósceles o equilátero.


#Función que determina si el triángulo es rectángulo.
def esRectangulo(ladoA, ladoB, ladoC):
    trianguloRectangulo = False

    if (ladoA**2 + ladoB**2 == ladoC**2) or (ladoA**2 + ladoC**2 == ladoB**2) or (ladoB**2 + ladoC**2 == ladoA**2):
        trianguloRectangulo = True

    return trianguloRectangulo


#Función que determina si el triángulo es isósceles.
def esIsosceles(ladoA, ladoB, ladoC):
    trianguloIsosceles = False

    if ladoA == ladoB and ladoA != ladoC:
        trianguloIsosceles = True
    elif ladoA == ladoC and ladoA != ladoB:
        trianguloIsosceles = True
    elif ladoB == ladoC and ladoB != ladoA:
        trianguloIsosceles = True

    return trianguloIsosceles


#Función que determina si el triángulo es equilátero.
def esEquilatero(ladoA, ladoB, ladoC):
    trianguloEquilatero = False

    if ladoA == ladoB and ladoB == ladoC:
        trianguloEquilatero = True

    return trianguloEquilatero


#Función que determina si el triángulo existe.
def determinarSiExiste(ladoA, ladoB, ladoC):
    trianguloExiste = False

    if (ladoA + ladoB) > ladoC and (ladoA + ladoC) > ladoB and (ladoB + ladoC) > ladoA:
        trianguloExiste = True

    return trianguloExiste


#Función principal. Lee e imprime datos.
def main():
    ladoA = int(input("Introduce el primer lado del triángulo: "))
    ladoB = int(input("Introduce el segundo lado del triángulo: "))
    ladoC = int(input("Introduce el tercer lado del triángulo: "))

    trianguloExiste = determinarSiExiste(ladoA, ladoB, ladoC)
    trianguloRectangulo = esRectangulo(ladoA, ladoB, ladoC)
    trianguloIsosceles = esIsosceles(ladoA,ladoB, ladoC)
    trianguloEquilatero = esEquilatero(ladoA, ladoB, ladoC)

    print()

    if trianguloExiste == True:
        if trianguloRectangulo == True:
            print("Es un triángulo rectángulo")
        elif trianguloIsosceles == True:
            print("Es un triángulo isósceles")
        elif trianguloEquilatero == True:
            print("Es un triángulo equilátero")
    else:
        print("Estos lados no corresponden a un triángulo")


#Llamar a la función principal.
main()
