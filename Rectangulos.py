# Autor: Juan Sebastián Lozano Derbez
# Calcula y compara las dimensiones de dos rectángulos

def calcularArea(ancho1, alto1, alto2, ancho2):         #Se calculan las 2 areas y se regresan sus valores
    area1 = ancho1 * alto1
    area2 = ancho2 * alto2

    return area1, area2


def calcularPerimetro(ancho1, alto1, alto2, ancho2):    #Se calculan ambos perimetros y se regresan sus valores
    perimetro1 = ancho1*2 + alto1*2
    perimetro2 = ancho2*2 + alto2*2

    return perimetro1, perimetro2


def compararRectiangulos(area1, area2):
    if area2 == area1:
        return "Las áreas son iguales"
    else:
        if area2 > area1:
            return "El área 2 es mayor"
        return "El área 1 es mayor"


def main():                                                                 #Se reciben los valores de los rectángulos y se ejecutan las funciones
    ancho1 = float(input("Inserte el ancho del primer rectángulo: "))
    alto1 = float(input("Inserte el alto del primer rectángulo: "))
    ancho2 = float(input("Inserte el ancho del segundo rectángulo: "))
    alto2 = float(input("Inserte el alto del segundo rectángulo: "))

    area1, area2 = calcularArea(ancho1, alto1, ancho2, alto2)
    perimetro1, perimetro2 = calcularPerimetro(ancho1, alto1, ancho2, alto2)

    print("")
    print("El área del primer rectángulo es %.2f"% area1)
    print("El área del segundo rectángulo es %.2f"% area2)
    print("")
    print("El perímetro del primer rectángulo es %.2f"% perimetro1)
    print("El perímetro del segundo rectángulo es %.2f"% perimetro2)

    compara = compararRectiangulos(area1, area2)

    print("-----------------------")
    print(compara)

main()