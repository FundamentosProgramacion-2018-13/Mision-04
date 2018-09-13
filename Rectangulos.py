# Carlos Badillo García
# Programa que lee las dimensiones de dos rectángulos y calcula e imprime el perímetro y el área de cada uno


def calcularArea(baseRec, alturaRec): #Calcular el área del rectángulo
    areaR = baseRec * alturaRec
    return areaR


def calcularPerimetro(baseRec, alturaRec): #Calcular el perímetro del rectángulo
    perimetroR = (baseRec*2) + (alturaRec*2)
    return perimetroR


def indicarRectanguloAreaMayor(areaR1, areaR2): #Indicar que rectángulo tiene mayor área o si tienen la misma área
    if areaR1 > areaR2:
        return "El área del primer rectángulo es mayor"
    elif areaR2 > areaR1:
        return "El área del segundo rectángulo es mayor"
    return "El área de ambos rectángulos es la misma"


def main(): #Usuario ingresa base y altura de ambos rectángulos, luego imprime el área y perimetro de ambos y por ultimo indica cual rectángulo tiene mayor área
    basePrimerRec = int(input("Teclea la base del primer rectángulo: "))
    alturaPrimerRec = int(input("Teclea la altura del primer rectángulo: "))
    print()
    baseSegundoRec = int(input("Teclea la base del segundo rectángulo: "))
    alturaSegundoRec = int(input("Teclea la altura del segundo rectángulo: "))
    perimetroR1 = calcularPerimetro(basePrimerRec, alturaPrimerRec)
    perimetroR2 = calcularPerimetro(baseSegundoRec, alturaSegundoRec)
    areaR1 = calcularArea(basePrimerRec, alturaPrimerRec)
    areaR2 = calcularArea(baseSegundoRec, alturaSegundoRec)
    areaMayor = indicarRectanguloAreaMayor(areaR1, areaR2)
    print()
    print("El perímetro del primer rectángulo es: ", perimetroR1)
    print("El perímetro del segundo rectángulo es: ", perimetroR2)
    print("El área del primer rectángulo es: ", areaR1)
    print("El área del segundo rectángulo es: ", areaR2)
    print()
    print(areaMayor)


main()