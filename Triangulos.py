#Autor: Marco González Elizalde
#Determina que tipo de triangulo es  en base a tres valores dados


#Determina si un triangulo es equilatero, isósceles, rectangulo o si no lo es dependiendo del valor de sus lados
def determinarTriangulo(ladoA, ladoB, ladoC):

    if(ladoA > 0 and ladoB > 0 and ladoC > 0):
        if(ladoA == ladoB):
            if(ladoA == ladoC):
                return "Es un triángulo equilatero"
            if(not ladoA == ladoC):
                return "Es un triángulo isósceles"

        if(ladoA == ladoC):
            if(ladoA == ladoB):
                return "Es un triángulo equilatero"
            if (not ladoA == ladoB):
                return "Es un triángulo isósceles"

        if(ladoB == ladoC):
            if(ladoB == ladoA):
                return "Es un triángulo equilatero"
            if(not ladoB == ladoA):
                return "Es un triángulo isósceles"

        if(ladoA**2 == ladoB**2 + ladoC**2):
            return "Es un triángulo rectángulo"

        if(ladoB**2 == ladoA**2 + ladoC**2):
            return "Es un triángulo rectángulo"

        if(ladoC**2 == ladoA**2 + ladoB**2):
            return "Es un triángulo rectángulo"

        return"Estos valores no corresponden a un triángulo"

    else:
        return"Estos valores no corresponden a un triángulo"


#Función principal, recibe el valor de los lados de un triangulo y regresa el tipo de triangulo
def main():
    ladoA = float(input("Teclee el largo del lado 1: "))
    ladoB = float(input("Teclee el largo del lado 2: "))
    ladoC = float(input("Teclee el largo del lado 3: "))

    tipoTriangulo = determinarTriangulo(ladoA, ladoB, ladoC)
    print("")
    print(tipoTriangulo)


#Corre el programa principal
main()
