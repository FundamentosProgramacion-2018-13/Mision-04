#Arturo Márquez Olivar. A01376086.
#Lee los datos y revisa si son de un triángulo Isosceles, Equilatero o Rectángulo, si no es ninguno de esos, manda un mensaje diferente.


#Identifica el tipo de triángulo según sus lados.
def identificadorDeTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return ("equilatero")
    else:
        if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return ("isosceles")
        else:
            return ("rectángulo")


#Se encarga de recibir los lados del triángulo y de imprimir si es o no es triángulo para poder imprimir el tipo de triángulo
def main():
    lado1 = int(input("Teclea la medida del lado 1. No importa el orden de los lados. "))
    lado2 = int(input("Teclea la medida del lado 2."))
    lado3 = int(input("Teclea la medida del lado 3."))
    
    triangulo = identificadorDeTriangulo(lado1, lado2, lado3)

    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print("Las medidas que ingresaste pertenecen a un triángulo %s." % (triangulo))
    else:
        print("Estos lados no corresponden a un triángulo.")
    
    
#Llamada a la función main.
main()