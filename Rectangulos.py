# Alex Fernando Leyva Martinez - A01747078 - Grupo: 04
# Calcula el área y perimetro de dos rectángulos y define cual de ambos es mayor.


#Calcula el área del rectángulo 1
def calcularArea1(largo1, ancho1):
    area1 = largo1 * ancho1
    return area1


#Calcula el Perimetro del rectángulo 1
def calcularPerimetro1(largo1, ancho1):
    perimetro1 = (largo1*2 + ancho1*2)
    return perimetro1


#Calcula el área del rectángulo 2
def calcularArea2(largo2, ancho2):
    area2 = largo2 * ancho2
    return area2


#Calcula el Perimetro del rectángulo 2
def calcularPerimetro2(largo2, ancho2):
    perimetro2 = (largo2*2 + ancho2*2)
    return perimetro2


#Calcula que rectángulo tiene el área más grande
def arearectangulo (area1, area2):
    if (area1 > area2):
        return "Rectangulo 1"
    if (area1 == area2):
        return "Ninguno ambos son iguales"
    else:
        return "Rectangulo 2"

    
# Lee los datos e imprime las áreas y perimetros además de que evalúa el área de los dos rectángulos e imprime el mayor
def main():
    largo1 = float(input("Ingresa el largo del rectangulo 1 en m: "))
    ancho1 = float(input("Ingresa el ancho del rectangulo 1 en m: "))
    largo2 = float(input("Ingresa el largo del rectangulo 2 en m: "))
    ancho2 = float(input("Ingresa el ancho del rectangulo 2 en m: "))
    area1 = calcularArea1(largo1, ancho1)
    area2 = calcularArea2(largo2, ancho2)
    perimetro1 = calcularPerimetro1(largo1, ancho1)
    perimetro2 = calcularPerimetro2(largo2, ancho2)
    area = arearectangulo(area1, area2)
    print("El área del rectángulo 1 es en cm:%.2f" % area1)
    print("El área del rectángulo 2 es en cm:%.2f" % area2)
    print("El perimetro del rectángulo 1 es en cm:%.2f" % perimetro1)
    print("El perimetro del rectángulo 2 es en cm:%.2f" % perimetro2)
    print("El Rectángulo que tiene mayor área es en cm:", area)

    
#Llama a la función principal
main()
