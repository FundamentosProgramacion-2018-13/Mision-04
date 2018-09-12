# Alex Fernando Leyva Martinez - A01747078 - Grupo: 04
# Este programa lee las longitudes de los triángulos para definir su tipo


#Verifica el tipo del triángulo comparando los valores de sus lados
def verificarTriangulo(lado1, lado2, lado3):
    if lado1 + lado2 + lado3 <= 0:
        return "Estos lados no corresponden a ningún triángulo"
    elif lado1**2 + lado2**2 == (lado3**2) or lado1**2 + lado2**2 == (lado3**2) or lado1**2 + lado3**2 == (lado1**2) or lado3**2 + lado2**2 == (lado1**2):
        return "Es Triángulo Rectángulo"
    elif lado1 == lado2 == lado3:
        return "Es Triángulo Equilatero"
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        return "Es Triángulo Isósceles"
    elif lado1 != lado2 != lado3:
        return "Estos lados no corresponden a ningún triángulo"

    
# Lee los valores de los lados y llama a la función que imprime el tipo de triángulo
def main():
    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))
    triangulo = verificarTriangulo(lado1, lado2, lado3)
    print(triangulo)

    
# Función principal
main()
