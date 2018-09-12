#Autor: Jesus Zabdiel Sánchez Chávez
#Descripción: Calcula el área u y perímetro de dos rectángulos cuyos lados son dados por el usuario y al final se dice
#si los rectángulos son iguales, el mayor o el menor.

#Calcula el área de n rectángulo
def calcularArea(base, altura):
    return base * altura


#Calcula el perímetro de un rectángulo
def calcularPerimetro(base, altura):
    return  (2*base) + (2*altura)


def main():
    baseUno = int(input("Inserta el valor de la base del primer rectángulo: "))
    alturaUno = int(input("Inserta el valor del altura del primer rectángulo: "))
    baseDos = int(input("Inserta el valor de la base del segundo rectángulo: "))
    alturaDos = int(input("Inserta el valor de la aluta del segundo rectángulo: "))
    areaUno = calcularArea(baseUno,alturaUno)
    areaDos = calcularArea(baseDos,alturaDos)
    perimetroUno = calcularPerimetro(baseUno,alturaUno)
    perimetroDos = calcularPerimetro(baseDos, alturaDos)
    print ("Perímetro del rectángulo uno: %.2f " % perimetroUno)
    print("Área del rectángulo uno: %.2f " % areaUno)
    print("Perímetro del rectángulo dos: %.2f " % perimetroDos)
    print("Área del rectángulo dos: %.2f " % areaDos)
    if areaUno > areaDos:
        print("El rectángulo uno tiene mayor área")
    else:
        if areaUno < areaDos:
            print("El rectángulo dos tiene mayor área")
        else:
            print ("Ambas áreas son iguales")

main()
