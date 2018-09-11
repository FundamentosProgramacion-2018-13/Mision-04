#Jesús Roberto Herrera Vieyra // A01377230
#Progrma que lee las dimensiones y calcula el perímetro y área de dos rectángulos indicando cual es más grande


#función para calcular área
def calcularArea(base, altura):
    area= base*altura
    return area


#función para calcular perímetro
def calcularPerimetro(base, altura):
    perimetro= 2*base+2*altura
    return perimetro


#función para elegir qué área es mayor
def elegirAreaMayor(area1, area2):
    if area1>area2:
        return area1
    if area2>area1:
        return area2
    return "Son iguales"


def main():
    base1= int(input("Introduce la medida de la base del primer rectaágulo: "))
    altura1= int(input("introduce la medida de la altura del primer rectaágulo: "))
    base2 = int(input("Introduce la medida de la base del segundo rectángulo: "))
    altura2 = int(input("introduce la medida de la altura del segundo rectángulo: "))

    area1= calcularArea(base1,altura1)
    perimetro1= calcularPerimetro(base1,altura1)
    area2 = calcularArea(base2, altura2)
    perimetro2 = calcularPerimetro(base2, altura2)
    areaMayor = elegirAreaMayor(area1,area2)

    print("área del primer rectángulo = %d m^2" %(area1))
    print("perímetro del primer rectángulo = %d m^2" % (perimetro1))
    print("área del segundo rectángulo = %d m^2" % (area2))
    print("perímetro del segundo rectángulo = %d m^2" % (perimetro2))

    if areaMayor == area1:
        print("El área del rectángulo 1 es más grande")

    if areaMayor == "Son iguales":

        print("Las áreas son iguales")

    if areaMayor == area2:
        print("El área del rectángulo 2 es más grande")


main()