#Jocelyn López Ortíz A01377451
#Clasificar un triángulo en rectángulo, isósceles o equilátero


def esEquilatero(lado1, lado2, lado3): #Función para saber si el triángulo es equilatero
    if lado1 == lado2 and lado1 == lado3:
        return True
    return False


def esIsosceles(lado1, lado2, lado3):  #Función para saber si el triángulo es isósceles
    if lado1 == lado2 and not lado1 == lado3:
        return True
    if lado1 == lado3 and not lado1 == lado2:
        return True
    if lado3 == lado2 and not lado1 == lado3:
        return True
    return False


def esRectangulo(lado1, lado2, lado3):  #Función para saber si el triángulo es rectángulo
    if lado1>lado2 and lado1>lado3:
        if lado1**2 ==(lado2**2 + lado3**2):
            return True
    if lado2>lado1 and lado2>lado3:
        if lado2**2 ==(lado1**2 + lado3**2):
            return True
    if lado3>lado1 and lado3> lado2:
        if lado3**2 ==(lado2**2 + lado1**2):
            return True
    return False


def claisificarTriangulo(lado1, lado2, lado3): #Funcion para calsificar el triángulo en rectángulo, isósceles, equilátero o nnguno
    tipoDeTriangulo = esRectangulo(lado1, lado2, lado3)
    if tipoDeTriangulo == True:
        return "Rectángulo"
    tipoDeTriangulo = esIsosceles(lado1, lado2, lado3)
    if tipoDeTriangulo == True:
        return "Isósceles"
    tipoDeTriangulo = esEquilatero(lado1, lado2, lado3)
    if tipoDeTriangulo == True:
        return "Equilátero"
    return 0


def main():
    lado1 = int(input("Valor del lado 1: "))
    lado2 = int(input("Valor del lado 2: "))
    lado3 = int(input("Valor del lado 3: "))

    tipoDeTriangulo = claisificarTriangulo(lado1, lado2, lado3)
    if not tipoDeTriangulo == 0:
        print("Tipo de triángulo: ", tipoDeTriangulo)
    else:
        print("Estos lados no corresponden a ningun triángulo")


main()