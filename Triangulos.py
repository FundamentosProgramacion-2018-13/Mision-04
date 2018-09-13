# Carlos Badillo García
# Programa que lee el valor de cada uno de los lados de un triangulo e indica el tipo de triángulo que es


def indicarTipoTriangulo(lado1, lado2, lado3): #Indicar que tipo de triángulo es dependiendo el valor de sus lados
    if lado1 == lado2 == lado3:
        return "El triángulo es equilátero"
    elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado1 != lado2 or lado2 == lado3 and lado2 != lado1:
        return "El triángulo es isósceles"
    elif lado1**2 == lado2**2 + lado3**2 or lado2**2 == lado1**2 + lado3**2 or lado3**2 == lado1**2 + lado2**2:
        return "El triángulo es rectángulo"
    else:
        return "Estos lados no corresponden a un triángulo"


def main(): # El usuario introduc el valor de lado 1, lado 2 y lado 3, luego imprime que tipo de triángulo
    lado1 = int(input("Teclea valor del lado1: "))
    lado2 = int(input("Teclea valor del lado2: "))
    lado3 = int(input("Teclea valor del lado3: "))
    tipoTriangulo = indicarTipoTriangulo(lado1, lado2, lado3)
    print (tipoTriangulo)


main()