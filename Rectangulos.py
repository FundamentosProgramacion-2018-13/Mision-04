###Autor: Jose Luis Mata Lomeli
###Calcular Area y Perimetro de dos rectángulos y comparar cual tiene mayor area o si es igual

##Calcular el Area y Perimetro del 1er Rectangulo:
#Area del 1er Rectángulo
def rectangulo1Area(rectArea1_1, rectArea2_1):

    area1 = rectArea1_1 * rectArea2_1
    return area1

#Perimetro del 1er Rectángulo
def rectangulo1Perimetro(rectPeri1_1, rectPeri2_1):

    perimetro1 = 2*(rectPeri1_1 + rectPeri2_1)
    return perimetro1


##Calcular Area y Perimetro del 2do Rectangulo:
#Area del 2do rectángulo
def rectangulo2Area(rectArea1_2, rectArea2_2):

    area2 = rectArea1_2 * rectArea2_2
    return area2

#Perimetro del 2do rectángulo
def rectangulo2Perimetro(rectPeri1_2, rectPeri2_2):

    perimetro2 = 2 *(rectPeri1_2 + rectPeri2_2)
    return perimetro2

##Compara las Areas de ambos rectángulos:
def compararAreas (a1, a2):

    if a1 > a2:
        return ("el 1er rectangulo; con %d de area" % (a1))
    else:
        if a2 > a1:
            return ("el 2do rectangulo; con %d de area" % (a2))
        else:
            if a1 == a2:
                return ("ninguna. El 1er y 2do rectangulo tienen la misma area")

##Comparar los Perimetros de Ambos rectangulos
def compararPerimetros(p1, p2):
    if p1 > p2:
        return ("el 1er rectangulo; con %d de perimetro" % (p1))
    else:
        if p2 > p1:
            return ("el 2do rectangulo; con %d de perimetro" % (p2))
        else:
            if p1 == p2:
                return ("ninguno. El 1er y 2do rectangulo tienen el mismo perimetro")


###Función principal
def main():

       dimension1_1 = int(input("Escriba la base del 1er rectangulo: "))
       dimension2_1 = int(input("Escriba la altura del 1er rectangulo: "))
