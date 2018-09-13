# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que lee el valor de los lados de un triángulo.


# La siguiente función determina el tipo de triángulo.
def tipoDeTriangulo(a, b, c):
    if (a > 0) and (b > 0) and (c > 0):
        if a == b == c:
            return "Los lados corresponden a un triángulo equilátero"
        elif c != a != b != c:
            return "Los lados corresponden a un triángulo rectangúlo"
        elif a == b != c or a != b == c or b != c == a:
            return "Los lados corresponden a un triángulo isósceles"
    else:
        return "Estos lados no corresponden a un triángulo"


# La función principal lee los valores de los lados del triángulo e imprime el resultado.
def main():
    ladoNumero1 = int(input("Primer lado del triángulo:  "))
    ladoNumero2 = int(input("Segundo lado del triángulo: "))
    ladoNumero3 = int(input("Tercer lado del triángulo: "))
    resultado = tipoDeTriangulo(ladoNumero1, ladoNumero2, ladoNumero3)
    print(resultado)


# Llama a la función principal.
main()