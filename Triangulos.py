#Autor: Samantha Martínez Franco A01747686
#Escribir el nombre del triangulo dependiendo del valor de sus lados


#Calcular que tipo de triangulo es dependiendo a sus lados
def definirTriangulo(lado1,lado2,lado3):
    if lado1==lado2==lado3:
        return "Triángulo Equilatero"
    elif (lado1==lado2 and lado2!=lado3) or (lado2==lado3 and lado2!=lado1) or (lado1==lado3 and lado1!=lado2):
        return "Triángulo Isósceles"
    elif lado1**2==lado2**2+lado3**2 or lado2**2==lado1**2+lado3**2 or lado3**2==lado1**2+lado2**2:
        return "Triángulo Rectángulo"
    else:
        return "Estos lados no corresponden a un triángulo"


#funcion principal
def main():
    lado1=int(input("¿Cual es el valor del lado 1? "))     #pedir valores
    lado2 = int(input("¿Cual es el valor del lado 2? "))
    lado3 = int(input("¿Cual es el valor del lado 3? "))
    triangulo=(definirTriangulo(lado1,lado2,lado3))      #pedir resultado de función de definir triangulos
    print((triangulo))           #imprimir resultados


main()

