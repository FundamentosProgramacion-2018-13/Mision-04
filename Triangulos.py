# Autor: David Isaí López Jaimes             A01748363
# Da el tipo de triangulo dependiendo el valor sus lados


def tipoTriangulo(a, b, c):    # Clasifica el tipo de triangulo comparando sus lados
    if a==b and b==c:
        tipo = "Equilátero"
    if a==b and b!=c or c==a and a!=b or c==b and a!=c:
        tipo = "Isóceles"
    if a != b and a != c and b != c :
        tipo = "Rectangulo"
    return tipo


def main():        # Aquí leemos y calculamos la funcion anterior e imprimimos resultados
    lado1 = int(input("Teclea el valor del lado 1: "))
    lado2 = int(input("Teclea el valor del lado 2: "))
    lado3 = int(input("Teclea el valor del lado 3: "))

    triangulo = tipoTriangulo(lado1, lado2, lado3)
    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Estos lados no corresponden a un triangulo")
    else:
        print("Tipo de triangulo: ", triangulo)

main()