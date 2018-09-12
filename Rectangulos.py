#Autor: David Rodriguez
#Lee las dimensiones y calcula el área y perímetro de dos rectángulos


#Calcula las áreas multiplicando su base por su altura
def calcularAreas(base, altura):
    area = base*altura
    return area

#Calcula cual de las áreas es mayor en base a su longitud
def calcularMayor(area1, area2):
    if area1 > area2:
        mayor = "El rectángulo 1 tiene un área mayor al rectángulo 2"
    elif area1 == area2:
        mayor = "Ambas áreas son iguales"
    else:
        mayor = "El rectángulo 2 tiene un área mayor al rectángulo 1"
    return mayor


#Calcula los perímetros de ambos rectángulos multiplicando los lados individualmente por dos y luego sumándolos
def calcularPerimetros(base, altura):
   perimetro = (base*2) + (altura*2)
   return perimetro


#Función principal
def main():
    base1 = int(input("Dame la base del primer rectángulo: "))
    altura1 = int(input("DAme la altura del primer rectángulo: "))
    base2 = int(input("Dame la base del segundo rectángulo: "))
    altura2 = int(input("DAme la altura del segundo rectángulo: "))
    area1 = calcularAreas(base1, altura1)
    area2 = calcularAreas(base2, altura2)
    mayor = calcularMayor(area1, area2)
    perimetro1 = calcularPerimetros(base1, altura1)
    perimetro2 = calcularPerimetros(base2, altura2)
    print("Rectángulo 1: ")
    print("Base= ", base1)
    print("Altura= ", altura1)
    print("Área= ", area1)
    print("Perímetro= ", perimetro1)
    print("Rectángulo 2: ")
    print("Base= ", base2)
    print("Altura= ", altura2)
    print("Área= ", area2)
    print("Perímetro= ", perimetro2)
    print(mayor)


main()