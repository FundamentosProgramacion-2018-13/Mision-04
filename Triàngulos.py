#Autor: Alberto Contreras Torres
#El programa recibe medidas de lado de un trianguloy despliega el tipo de triàngulo que es

#Recibe lados y regresa tipo de triàngulo
def definirTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        print("El triàngulo es equilatero")
    elif lado1 == lado2 and lado1 != lado3:
        print("El triàngulo es Isòsceles")
    elif lado1!= lado2 and lado2!=lado3:
        print("El triàngulo es Rectangulo")
    else:
        print("ERROR")



#Funciòn principal
def main():
    lado1= int(input("Teclea medida de el lado1: "))
    lado2= int(input("Teclea medida de el lado2: "))
    lado3= int(input("Teclea medida de el lado3: "))
    tipoTriangulo= definirTriangulo(lado1, lado2, lado3)


main()