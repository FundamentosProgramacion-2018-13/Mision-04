#Autor: Diana Marisol Medina Bravo
#Lee las dimensiones de dos rectángulos y que calcula e imprima el perímetro y área de cada uno. Tambien indica cual tiene mayor area
#o si son iguales

#Función para calcular el área del rectángulo 1
#Recibe el valor de las dimensiones del primer rectangulo y regresa el área 1
def calcularArea1 (lado1Rectangulo1,lado2Rectangulo1):
    area1=lado1Rectangulo1*lado2Rectangulo1
    return area1


#Función para calcular el área del rectángulo 2
#Recibe el valor de las dimensiones del segundo rectángulo y regresa el área 2
def calcularArea2 (lado1Rectangulo2,lado2Rectangulo2):
    area2= lado1Rectangulo2 * lado2Rectangulo2
    return area2


#Función para calcular el perímetro del rectangulo 1
#Recibe el valor de las dimensiones del primer rectángulo y regresa el perímetro 1
def calcularPerimetro1 (lado1Rectangulo1,lado2Rectangulo1):
    perimetro1=(2*lado1Rectangulo1)+(2*lado2Rectangulo1)
    return perimetro1


#Función para calcular el perímetro del rectangulo 2
#Recibe el valor de las dimensiones del segundo rectángulo y regresa el perímetro 2
def calcularPerimetro2 (lado1Rectangulo2,lado2Rectangulo2):
    perimetro2 = (2 * lado1Rectangulo2) + (2 * lado2Rectangulo2)
    return perimetro2


#Función principal
def main():
    lado1Rectangulo1=int(input("Teclee el valor del lado 1 del primer rectángulo: "))
    lado2Rectangulo1=int(input("Teclee el valor del lado 2 del primer rectángulo: "))
    lado1Rectangulo2=int(input("Teclee el valor del lado 1 del segundo rectángulo: "))
    lado2Rectangulo2=int(input("Teclee el valor del lado 2 del segundo rectángulo: "))
    area1=calcularArea1(lado1Rectangulo1,lado2Rectangulo1)
    area2=calcularArea2(lado1Rectangulo2, lado2Rectangulo2)
    perimetro1=calcularPerimetro1(lado1Rectangulo1,lado2Rectangulo1)
    perimetro2=calcularPerimetro2(lado1Rectangulo2,lado2Rectangulo2)
    print("")
    print ("El área del primer rectángulo es: ",area1)
    print("El perímetro del primer rectángulo es: ", perimetro1)
    print("")
    print("El área del segundo rectángulo es: ", area2)
    print("El perímetro del segundo rectángulo es: ",perimetro2)
    print("")
    if area1 > area2:
        print("El área del primer rectángulo es mayor a la del segundo")
    if area2 > area1:
        print("El área del segundo rectángulo es mayor a la del primero")
    if area1==area2:
        print("Las áreas son iguales")


main()