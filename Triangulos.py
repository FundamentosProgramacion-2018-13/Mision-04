#Autor: Alejandro Torices Oliva
#Programa que identifica de que tipo de triángulo se trata conociendo el valor de sus lados.

#Identifica el tipo de triángulo comparando sus lados.
def identificarTriangulo(a, b, c):
    if a == b and b == c:
        return "Es un triángulo equilátero."
    elif (a**2) == (b**2)+(c**2) or (b**2) == (c**2)+(a**2) or (c**2) == (a**2)+(b**2):
        return "Es un triángulo rectángulo."
    elif a == b or b == c or a == c:
        return "Es un triángulo isóceles."
    else:
        return "Es un triángulo escaleno."


#Función principal.
def main():
    a = int(input("""Ingrese el lado "a" del triángulo: """))
    b = int(input("""Ingrese el lado "b" del triángulo: """))
    c = int(input("""Ingrese el lado "c" del triángulo: """))

    print(" ")

    if a <= 0 or b <= 0 or c <= 0:
        print("Estos lados no corresponden a un triángulo.")
    else:
        tipoTriangulo = identificarTriangulo(a, b, c)
        print(tipoTriangulo)


main()