# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Confirma si existe el triángulo y qué tipo es


#Checa si es un triángulo rectángulo
def esTrianguloRectangulo(a, b, c):
    if (((a ** 2)+(b ** 2)) == c ** 2) or (((a ** 2) + (c ** 2)) == b ** 2) or (((b ** 2) + (c ** 2)) == a ** 2):
        return True
    return False


#Cadena de comparaciones entre lados para saber el tipo de triángulo que es
def checarTipoDeTriangulo(a, b, c):
    if (a == b) and (a == c):
         return "Es un triángulo equilatero"
    if esTrianguloRectangulo(a, b, c):
        return "Es un triangulo rectángulo"
    if (a == b) or (a == c) or (b == c):
        return "Es un triangulo isóceles"
    else:
        return "El triángulo no existe"


#Obtiene datos e imprime resultados
def main():
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))

    print(checarTipoDeTriangulo(a, b, c))


#Ejecuta la función main
main()
