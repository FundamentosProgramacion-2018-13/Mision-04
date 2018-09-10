"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998
Descripción: Calcula el área y el perímetro de un rectángulo con base en los lados introducidos.

"""

#Calcula el area con base a los lados del rectánuglo
def calcularArea(lado1, lado2):
    area = lado1*lado2
    return area


#Calcula el perímetro con base a los lados del rectánuglo
def calcularPerimetro(lado1, lado2):
    perimetro = 2*lado1 + 2*lado2
    return perimetro


#Compara las áreas para determinar cual área de los rectángulos es mayor
def definirAreaMayor(area1, area2):
    if area1 > area2:
        return "Rectánuglo 1"
    if area2 > area1:
        return "Rectángulo 2"
    if area1 == area2:
        return "Los rectánuglos son iguales"


#Imprime todos los resultados de área, perímetro y área mayor
def imprimir(lado1, lado2, lado3, lado4, area1, area2):
    print("Area del Rectángulo 1: {:.2f}" .format(calcularArea(lado1, lado2)))
    print("Area del Rectángulo 2: {:.2f}" .format(calcularArea(lado3, lado4)))
    print("Perímetro del Rectángulo 1: {:.2f}" .format(calcularPerimetro(lado1, lado2)))
    print("Perímetro del Rectángulo 1: {:.2f}" .format(calcularPerimetro(lado3, lado4)))
    print(" Mayor área: {}" .format(definirAreaMayor(area1, area2)))


#Engloba todas las instrucciones anteriores para resolver el problema
def main():
    lado1 = float(input("Lado 1 del rectángulo 1: "))
    lado2 = float(input("Lado 2 del rectángulo 1: "))
    lado3 = float(input("Lado 1 del rectángulo 2: "))
    lado4 = float(input("Lado 2 del rectángulo 2: "))
    if (lado1 <= 0) or (lado2 <= 0) or (lado3 <= 0) or (lado4 <= 0):
        return print("Una de las figuras no existe")
    area1 = calcularArea(lado1, lado2)
    area2 = calcularArea(lado3, lado4)
    perimetro1 = calcularPerimetro(lado1, lado2)
    perimetro2 = calcularPerimetro(lado3, lado4)
    imprimir(lado1, lado2, lado3, lado4, area1, area2)


#Ejecuta la función main para resolver el problema
main()