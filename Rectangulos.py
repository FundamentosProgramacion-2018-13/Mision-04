#Autor: Víctor Manuel Rodríguez Loyola
#Cálculo del área de 2 rectángulos y comparación de las mismas


def CalcularPerimetro1(base1, altura1): #Calcula el perímetro del rectángulo 1 dadas su base y su altura.
    perimetro1 = (2*base1) + (2*altura1)
    return perimetro1


def CalcularArea1(base1, altura1): #Calcula el área del rectángulo 1 dadas su base y su altura.
    area1= base1 * altura1
    return area1


def CalcularPerimetro2(base2, altura2):  #Calcula el perímetro del rectángulo 2 dadas su base y su altura.
    perimetro2= (2*base2) + (2*altura2)
    return perimetro2


def CalcularArea2(base2, altura2): #Calcula el área del rectángulo 2 dadas su base y su altura.
    area2= base2 * altura2
    return area2


def EncontrarAreaMayor(AreaRect1, AreaRect2): #Compara las áreas obtenidas para saber cuál es la mayor, o si son iguales.
    if AreaRect1 > AreaRect2:
        return "El primer rectángulo tiene mayor área"
    else:
        if AreaRect2 > AreaRect1:
            return "El segundo rectángulo tiene mayor área"
        else:
            return "Las áreas son iguales"


def main():
    baseRectangulo1=int(input("Teclea la base del primer rectánculo: "))
    alturaRectangulo1 = int(input("Teclea la altura del primer rectángulo: "))
    baseRectangulo2=int(input("Teclea la base del segundo rectángulo: "))
    alturaRectangulo2 = int(input("Teclea la altura del segundo rectángulo: "))

    PerimetroRectangulo1= CalcularPerimetro1(baseRectangulo1,alturaRectangulo1)
    AreaRectangulo1= CalcularArea1(baseRectangulo1,alturaRectangulo1)
    PerimetroRectangulo2= CalcularPerimetro2(baseRectangulo2, alturaRectangulo2)
    AreaRectangulo2= CalcularArea2(baseRectangulo2, alturaRectangulo2)
    AreaMayor= EncontrarAreaMayor(AreaRectangulo1, AreaRectangulo2)

    print("El perímetro del rectángulo 1 es: %.2f"%PerimetroRectangulo1)
    print("El área del rectángulo 1 es: %.2f"%AreaRectangulo1)
    print("\nEl perímetro del rectángulo 2 es: %.2f"%PerimetroRectangulo2)
    print("El área del rectángulo 2 es: %.2f"%AreaRectangulo2)
    print("\n",AreaMayor)


main()
