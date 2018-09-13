#Autor: Jesús Emmanuel Alcalá Nava
#Descripción: este programa determina el tipo de triángulo a partir de los lados dados por el usuario


def determinarTriangulo(lado1, lado2, lado3): #determina qué tipo de triángulo es y si los valores no corresponden a un triángulo, te lo hace saber
     if(lado1 > 0 and lado2 > 0 and lado3 > 0):
        if(lado1 == lado1):
            if(lado1 == lado3):
                return "Triángulo equilatero"
            if(not lado1 == lado3):
                return "Triángulo isósceles"
        if(lado1 == lado3):
            if(lado1 == lado2):
                return "Triángulo equilatero"
            if (not lado1 == lado2):
                return "Triángulo isósceles"
        if(lado2 == lado3):
            if(lado2 == lado1):
                return "Triángulo equilatero"
            if(not lado2 == lado1):
                return "Triángulo isósceles"
        if(lado1**2 == lado2**2 + lado3**2):
            return "Triángulo rectángulo"
        if(lado2**2 == lado1**2 + lado3**2):
            return "Triángulo rectángulo"
        if(lado3**2 == lado1**2 + lado2**2):
            return "Triángulo rectángulo"
        return"Estos lados no corresponden a un triángulo"
     else:
        return"Estos lados no corresponden a un triángulo"


def main():
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    tipoDeTriangulo = determinarTriangulo(lado1, lado2, lado3)
    print(tipoDeTriangulo)
main()