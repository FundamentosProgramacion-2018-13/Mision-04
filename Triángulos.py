# Autor: Juan Sebastián Lozano Derbez
#Define el tipo de triángulo basado en sus medidas

def definirTriangulo(a, b, c):                                      #Serie de ifs con los que determinamos el tipo de triángulo
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        if a == b or a == c or b == c:
            return "Isóceles"
    if a == b == c:
        return "Equilatero"
    if (c == (a ** 2 + b ** 2) ** .5) or (b == (a**2 + c**2)**.5) or (a == (b**2 + c**2)**.5):
        return "Rectángulo"
    return "Triángulo no válido"


def main():                             #Se reciben las medidas, se ejecuta la función y se imprime
    ladoa = float(input("Lado a: "))
    ladob = float(input("Lado b: "))
    ladoc = float(input("Lado c: "))

    tipo = definirTriangulo(ladoa, ladob, ladoc)
    print(tipo)

main()