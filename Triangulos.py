# Alex Serrano Durán
# Este programa recibe los lados de un triángulo y calcula que tipo de triángulo es


def esRectangulo(lado1, lado2, lado3):         # Esta función verifica si el triángulo es rectángulo con T. de Pitágoras
    if lado1**2 == lado2 ** 2 + lado3 ** 2:
        return True
    if lado2 ** 2 == lado1 ** 2 + lado3 ** 2:
        return True
    if lado3 ** 2 == lado2 ** 2 + lado1 ** 2:
        return True


def esIsosceles(lado1, lado2, lado3):           # Esta función compara si dos lados son iguales (pero diferentes al
    if lado1 == lado2 != lado3:                 # tercero) para que se cumpla el isósceles
        return True
    if lado2 == lado3 != lado1:
        return True
    if lado1 == lado3 != lado2:
        return True


def esEquilatero(lado1, lado2, lado3):          # Esta función verifica si los tres lados son iguales, o lo que es lo
    if lado1 == lado2 == lado3:                 # mismo, un triángulo equilátero
        return True


def main():     # La función main verifica qué tipo de triángulo es o si no se cumple ninguno, y se imprime el resultado
    lado1 = int(input("Introduce el primer lado: "))
    lado2 = int(input("Introduce el segundo lado: "))
    lado3 = int(input("Introduce el tercer lado: "))
    if esRectangulo(lado1,lado2,lado3):
        print("El triángulo es rectángulo")
    if esIsosceles(lado1,lado2,lado3):
        print("El triángulo es isósceles")
    if esEquilatero(lado1,lado2,lado3):
        print("El triángulo es equilátero")
    if esRectangulo(lado1,lado2,lado3) is None and esIsosceles(lado1,lado2,lado3) is None and esEquilatero(lado1,lado2,lado3) is None:
        print("Estos lados no corresponden a un triángulo")


main()
