#Javier Alexandro Vargas Sánchez A01377718
#Programa que dados los 3 lados de un tringulo identifica que tipo de triangulo es rectángulo, equilatero o isósceles


#Función que sirve para identificar si se trata de un triangulo equilatero
def verificarSiEsEqui(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return True


#Función que a partir del teorema de pitágoras realiza una evaluación para determinar si se trata de un triángulo rect
#Es el ejemplo que hicieron Alek y Diego Palmerín en Clase
def verificarSiEsRect(lado1, lado2, lado3):
    if (lado1 ** 2) + (lado2 ** 2) == (lado3 **2):
        return True
    if (lado2 ** 2) + (lado3 ** 2) == (lado1 **2):
        return True
    if (lado1 ** 2) + (lado3 ** 2) == (lado2 **2):
        return True


#Función que sirve para identificar si se trata de un triángulo isósceles
def verificarSiEsIsos(lado1, lado2, lado3):
    if lado1 == lado2 != lado3:
        return True
    if lado2 == lado3 != lado1:
        return True
    if lado1 == lado3 != lado2:
        return True
    else:
        return False

#Función principal
def main():
    lado1 = int(input("Teclea la longitud de uno de los lados del triángulo: "))
    lado2 = int(input("Teclea la longitud de otro de los lados del triángulo: "))
    lado3 = int(input("Teclea la longitud del lado faltante del traingulo: "))

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
        print("Error, Estos lados no corresponden a un triángulo")
    else:
        if verificarSiEsEqui (lado1,lado2, lado3):
            print("Las medidas de estos lados corresponden a un triángulo equilatero")
        if verificarSiEsRect (lado1, lado2, lado3):
            print("Las medidas de estos lados corresponden a un triángulo rectángulo")
        if verificarSiEsIsos (lado1, lado2, lado3):
            print("Las medidas de estos lados corresponden a un triángulo isósceles")


#Llamada a la función main
main()