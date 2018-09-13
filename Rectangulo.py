#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripción: Programa que lea dimensiones de rectangulos, calcule are y perimetro. Indica que area es mayor o si son
#guales

#Calcula el perimetro usando la formula de 2largo + 2ancho
def calcularPerimetro1(lado1, lado2):
    perimetro1 = (2*lado1)+(2*lado2)
    return perimetro1

#Calcula el area del rectangulo usando la fomrula de largo*alto
def calcularArea1(lado1, lado2):
    area1 = lado1*lado2
    return area1

#Calcula el perimetro usando la formula de 2largo + 2ancho
def calcularPerimetro2(lado3, lado4):
    perimetro2 = (2*lado3)+(2*lado4)
    return perimetro2

#Calcula el area del rectangulo usando la fomrula de largo*alto
def calcularArea2(lado3, lado4):
    area2 = lado3*lado4
    return area2

#Indica mediante selección que area es mayor o si son iguales
def indicarAreaMayor(area1, area2):
    if area1 > area2:
       return "El area mayor es la del primer rectangulo"
    elif area1 == area2:
        return "Las areas son iguales"
    else:
        return "El area mayor es la segunda"


#Función principal
def main():
    lado1 = float(input("Ingresa el largo del primer rectangulo: "))
    lado2 = float(input("Ingresa el alto del primer rectangulo: "))
    print("...............")
    lado3 = float(input("Ingresa el largo del segundo rectangulo: "))
    lado4 = float(input("Ingresa el alto del segundo rectangulo: "))
    calcularPerimetro1(lado1, lado2)
    calcularArea1(lado1, lado2)
    calcularPerimetro2(lado3, lado4)
    calcularArea2(lado3, lado4)
    perimetro1 = calcularPerimetro1(lado1, lado2)
    perimetro2 = calcularPerimetro2(lado3, lado4)
    area1 = calcularArea1(lado1, lado2)
    area2 = calcularArea2(lado3, lado4)
    print("...............")
    print ("El perimetro del primer rectangulo es de: %.2f " % (perimetro1))
    print ("El area del primer rectangulo es de: %.2f" % (area1))
    print ("")
    print ("El perimetro del segundo rectangulo es de: %.2f " % (perimetro2))
    print ("El area del segundo rectangulo es de: %.2f" % (area2))
    print ("")
    print("...............")
    print ("")
    indicarAreaMayor(area1, area2)
    areaM = indicarAreaMayor(area1, area2)
    print (areaM)


main()





