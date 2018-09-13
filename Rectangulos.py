# Sebastian Macias - A01376492
# Calcula el perímetro y área y define que área es mayor.


# Calcular el perimetro de los rectángulos 
def calcularPerimetroRectangulo(base, altura):
    perimetro = ((2 * base) + (2 * altura))
    return perimetro


# Calcular el área de los rectángulos
def calcularAreaRectangulo(base, altura):
    area = base * altura
    return area


# Determina cuál rectángulo posee el área más grande
def buscarMayor(areaRectangulo1, areaRectangulo2):
    if areaRectangulo1 > areaRectangulo2:
        return "El área del primer rectángulo es mayor"
    else:
        if areaRectangulo1 < areaRectangulo2:
            return "El área del segundo rectángulo es mayor"
        else:
            return "Las áreas son iguales"



# Recibe los datos de la base y la altura, para después mandarlos a las funciones correspondientes y realice los cálculos.
def main():
    baseRectangulo1 = int(input("Escribe la base del primer rectángulo: "))
    alturaRectangulo1 = int(input("Escribe la altura del primer rectángulo: "))
    baseRectangulo2 = int(input("Escribe la base del segundo rectángulo: "))
    alturaRectangulo2 = int(input("escribe la altura del segundo rectángulo: "))

    perimetroRectangulo1 = calcularPerimetroRectangulo(baseRectangulo1, alturaRectangulo1)
    perimetroRectangulo2 = calcularPerimetroRectangulo(baseRectangulo2, alturaRectangulo2)
    areaRectangulo1 = calcularAreaRectangulo(baseRectangulo1, alturaRectangulo1)
    areaRectangulo2 = calcularAreaRectangulo(baseRectangulo2, alturaRectangulo2)

    print(" ")
    print("El perímetro del primer rectángulo es de ", perimetroRectangulo1, "unidades y el área es de ", areaRectangulo1, "unidades cuadradas")
    print("El perímetro del segundo rectángulo es de ", perimetroRectangulo2, "unidades y el área es de ", areaRectangulo2, "unidades cuadradas")
    print(buscarMayor(areaRectangulo1, areaRectangulo2))



main()
