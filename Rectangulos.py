# Autor: Oscar Macias Rodríguez
# Descripción: Lee las dimensiones de dos rectángulos y calcula e imprime el area y el perímetro.


# Función principal. Calcula áreas, perímetros e indica cuál área es mayor.
def main():
    lado1 = int(input("Escriba el lado del rectángulo: "))
    lado2 = int(input("Escriba la altura del rectángulo: "))

    print("Lado 1: ", lado1)
    print("Lado 2: ", lado2)
    calcularArea(lado1, lado2)
    calcularPerimetro(lado1, lado2)

    lado3 = int(input("Escriba el lado del rectángulo: "))
    lado4 = int(input("Escriba la altura del rectángulo: "))

    print("Lado 3: ", lado3)
    print("Lado 4: ", lado4)
    calcularArea1(lado3, lado4)
    calcularPerimetro1(lado3, lado4)

    compararAreas(lado1, lado2, lado3, lado4)


# Compara los resultados de las dos áreas.
def compararAreas(lado1, lado2, lado3, lado4):
    area1 = lado1*lado2
    area2 = lado3*lado4

    if area1 < area2:
        print("El rectángulo 2 tiene mayor área: ", area2)
    if area1 > area2:
        print("El rectángulo 1 tiene mayor área: ", area1)
    if area1 == area2:
        print(area1, "y", area2, "son iguales")


# Calcula el área del primer rectángulo.
def calcularArea(lado1, lado2):
    area1 = lado1 * lado2
    print("El área es: ", area1)
    return

# Calcula el área del segundo rectángulo.
def calcularArea1(lado3, lado4):
    area2 = lado3 * lado4
    print("El área es: ", area2)
    return


# Calcula el perímetro del primer rectángulo.
def calcularPerimetro(lado1, lado2):
    perimetro1 = 2*lado1 + 2*lado2
    print("El perímetro es: ", perimetro1)
    return


# Calcula el perímetro del segundo rectángulo.
def calcularPerimetro1(lado3, lado4):
    perimetro2 = 2*lado3 + 2*lado4
    print("El perímetro es: ", perimetro2)
    return


main()