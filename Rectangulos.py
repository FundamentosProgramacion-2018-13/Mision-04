#Arturo Márquez Olivar. A01376086.
#Recibe datos de 2 rectángulos e imprime el perímetro y el área de ambos.


#Calcula el perímetro del rectángulo 1.
def calcularPerimetro1(altura, base):
    perimetro = (2 * altura) + (2 * base)
    return perimetro


#Calcula el área del rectángulo 1.
def calcularArea1(altura, base):
    area = base * altura
    return area


#Calcula el perímetro del rectángulo 2.
def calcularPerimetro2(altura, base):
    perimetro = (2 * altura) + (2 * base)
    return perimetro


#Calcula el área del segundo rectángulo.
def calcularArea2(altura, base):
    area = base * altura
    return area


#Recibe los datos de los rectángulos e imprime perímetro y área. Ademas, revisa cuál tiene mayor área y lo imprime.
def main():
    altura1= float(input("¿Cuál es la altura del primer rectángulo?"))
    base1= float(input("¿Cuál es la base del primer rectángulo?"))
    altura2= float(input("¿Cuál es la altura del segundo rectángulo?"))
    base2= float(input("¿Cuál es la base del segundo rectángulo?"))

    perimetroRectangulo1= calcularPerimetro1(altura1, base1)
    areaRectangulo1= calcularArea1(altura1, base1)
    perimetroRectangulo2 = calcularPerimetro2(altura2, base2)
    areaRectangulo2 = calcularArea2(altura2, base2)

    print("""Del primer rectángulo:
    Perímtero = %.2f
    Área = %.2f
    """ % (perimetroRectangulo1, areaRectangulo1))

    print("""Del segundo rectángulo:
    Perímtero = %.2f
    Área = %.2f
    """ % (perimetroRectangulo2, areaRectangulo2))

    if areaRectangulo1 == areaRectangulo2:
        print("Las áreas de los rectángulos son iguales.")

    else:
        if areaRectangulo1 > areaRectangulo2:
           print("El primer rectángulo tiene mayor área.")
        print("El segundo rectángulo tiene mayor área.")


#Llama a la función main.
main()