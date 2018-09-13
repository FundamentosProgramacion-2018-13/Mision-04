#Autor: Luis Ricardo Chagala Cervantes.
#Determinar que tipo de triangulo es, referente a las medidas de los lados ingresados.


def calculoTriangulo(a, b, c):
    x = a**2
    y = b**2
    z = c**2
    if a <= 0 or b <= 0 or c <= 0:
        return "Estos lados no corresponden a un triángulo"
    if int(float(x+y)) == int(float(z))or int(float(x+z)) == int(float(y))or int(float(z+y)) == int(float(x)):
        return "Es un triangulo cuadrado"

    if int(float(a)) == int(float(b)) and int(float(a)) == int(float(c)):
        return "Es un triangulo Equilatero"

    if int(float(a)) == int(float(b)) or int(float(a)) == int(float(c))or int(float(b)) == int(float(c)):
        return "Es un triangulo Isósceles"
    else:
        return "Estos lados no corresponden a un triángulo"


def imprimir(triangulo):
    print(triangulo)


def main():
    a = float(input("Lado A: "))
    b = float(input("Lado b: "))
    c = float(input("Lado C: "))
    triangulo = calculoTriangulo(a, b, c)
    imprimir(triangulo)


main()
