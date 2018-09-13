#Damián Iván García Ravelo
#A01376354
#Programa que calcula el área y el perímetro de  dos rectángulos distintos

def calcularArea1 (lado1, lado2): #Calcula el área del primer rectángulo
    area1 = lado1 * lado2
    return area1


def calcularPerimetro1 (lado1, lado2): #Calcula el perímetro del primer rectángulo
    perimetro1 = 2*lado1 + 2*lado2
    return perimetro1

def calcularArea2 (lado3, lado4): #Calcula el área del segundo rectángulo
    area2 = lado3 * lado4
    return area2


def calcularPerimetro2 (lado3, lado4): #Calcula el perímetro del segundo rectángulo
    perimetro2 = 2*lado3 + 2*lado4
    return perimetro2


def main():
#Solicita al usuario teclear los lados de los rectángulos
    lado1 = float(input("Teclea un lado del primer rectángulo: "))
    lado2 = float(input("Teclea el otro lado del primer rectángulo: "))
    lado3 = float(input("Teclea un lado del segundo rectángulo: "))
    lado4 = float(input("Teclea el otro lado del segundo rectángulo: "))

#Declara a las nueva variables el valor de las funciones usadas anteriormente
    primerArea = calcularArea1(lado1, lado2)
    primerPerimetro = calcularPerimetro1(lado1, lado2)
    segundaArea = calcularArea2(lado3, lado4)
    segundoPerimetro = calcularPerimetro2(lado3, lado4)

#Imprime el área y el perímetro de los dos rectángulos
    print ("El área y perimetro del primer rectángulo so:", format(primerArea, ".2f"), "unidades cuadradas y ",format(primerPerimetro,".2f"), "unidades")
    print("El área y perimetro del segundo rectángulo son:", format(segundaArea, ".2f"), "unidades cuadradas y ",format(segundoPerimetro,".2f"), "unidades")

#Condicionales para ver cuál rectángulo es mayor
    if primerArea > segundaArea:
        print ("Area1 es mayor")
    elif primerArea < segundaArea:
        print ("Area 2 es mayor")
    elif primerArea == segundaArea:
        print ("Areas son iguales")

main () #Llama a la función principal