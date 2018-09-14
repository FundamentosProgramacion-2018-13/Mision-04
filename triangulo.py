# Autor: Danhel Alejandro Mercado Velasco
# Especifica si os lados son correspondientes a un triangulo equilatero
# rectangulo o isósceles

def tipoTriangulo(a, b, c):
    if (a > 0) and (b > 0) and (c > 0):
        if a == b == c:
            return "Corresponden a un triángulo equilatero"
        if c != a != b != c:
            return "Corresponden a un triángulo rectangúlo"
        if a == b != c or a != b == c or b != c == a:
            return "Corresponden a un triángulo isósceles"
    else:
        return "No corresponden a ningún tipo de triangulo"

# Función principal que pide los datos y los lados e imprime el resultado del tipo de triangulo.

def main():
    lado1 = int(input("Dame el primer lado: "))
    lado2 = int(input("Dame el segundo lado: "))
    lado3 = int(input("Dame el tercer lado: "))
    resultado = tipoTriangulo(lado1, lado2, lado3)
    print(resultado)
# Llamada a la función
main()