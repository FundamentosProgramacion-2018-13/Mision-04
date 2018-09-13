#Javier Alexandro Vargas Sánchez A01377718
'''Programa que calcula area y perimetro de dos rectangulos dados la base y altura; además compara sus áreas y define
cual es el rectángulo más grande'''

#Función para calcular el área dados la longitud de la base y de la altura
def calcularArea(base, alt):
    area = base * alt
    return area


#Función para calcular el perimetro dados la longitud de la base y de la altura
def calcularPerimetro(base, alt):
    perimetro = (base * 2) +(alt *2)
    return  perimetro


#Función que compara las áreas de ambos rectángulos y define el rectángulo más grande
def compararRectangulos(area1, area2):

    if area1 > area2:
        print("El área del primer rectángulo es más grande que el área del segundo rectángulo")
    if area1 < area2:
        print("El área del segundo rectángulo es más grande que el área del primer rectángulo")
    if area1 == area2:
        print("Ambos rectángulos tienen la misma área")




def main ():
    base1 = int(input("Teclea la longitud de la base del primer rectángulo: "))
    alt1 = int(input("Teclea la longitud de la altura del primer rectángulo: "))
    base2 = int(input("Teclea la longitud de la base del segundo rectángulo: "))
    alt2 = int(input("Teclea la longitud de la altura del segundo rectángulo: "))
    if base1 <=0 or alt1 <= 0 or base2 <=0 or alt2 <= 0:
        print("Error, al menos una de tus distancias no existe")
    else:
        area1 = calcularArea(base1, alt1)
        area2 = calcularArea(base2, alt2)
        perimetro1 = calcularPerimetro(base1, alt1)
        perimetro2 = calcularPerimetro(base2, alt2)
        print("El área del primer rectángulo es de: ", area1)
        print("El área del segundo rectángulo es de: ", area2)
        print("El perímetro del primer rectángulo es de: ", perimetro1)
        print("El perímetro del segundo rectángulo es de: ", perimetro2)
        rectMasGrande = compararRectangulos(area1, area2)
        print(rectMasGrande)


#Llamada a la función principal
main()


