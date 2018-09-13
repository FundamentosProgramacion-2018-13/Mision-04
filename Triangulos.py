# Autor: Oscar Macias Rodríguez
# Descripción: Lee el valor de cada uno de los lados del triángulo y escribe el tipo de triángulo.


# Función principal. Imprime el tipo de triangulo y recibe los 3 lados del triángulo.
def main():
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))

    definirTriangulo(lado1, lado2, lado3)


# Define que tipo de triángulo es dependiendo en las restricciones de sus lados.
def definirTriangulo(lado1, lado2, lado3):

    if (lado1 + lado2) < lado3 or (lado2 + lado3) < lado1 or (lado1 + lado3) < lado2:
        return print("El triángulo no existe")
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        return print("El triángulo no existe")
    if lado1 and lado2 <= 0:
        return print("El triángulo no existe")
    if lado1 and lado3 <= 0:
        return print("El triángulo no existe")
    if lado2 and lado3 <= 0:
        return print("El triángulo no existe")
    if lado1**2 == lado2**2 + lado3**2 or lado2**2 == lado1**2 + lado3**2 or lado3**2 == lado1**2 + lado2**2:
        print("Triángulo rectángulo")
    if lado1 == lado2 == lado3:
        print("Equilatero")
    if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
        print("Isóceles")


main()