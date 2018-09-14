# Autor: Luis Humberto Burgueño Paz
# El programa recibe las dimensiones de dos rectángulos y calcula e imprime el área y el perímetro de ambos, posteriormente indica cuál tiene mayor área


# Recibe como parámetros la base y la altura y regresa el área del rectángulo
def calcularArea(base, altura):
    area = base * altura
    return area


# Recibe como parámetros la base y la altura y regresa el perímetro del rectángulo
def calcularPerimetro(base, altura):
    perimetro = (2*base) + (2*altura)
    return perimetro


# Recibe como parámetros ambas áreas y regresa cuál rectángulo tiene una mayor áreeao si son iguales
def sacarMayor(area1, area2):
    if area1 > area2:
        return "El rectángulo 1 tiene un área mayor que el rectángulo 2"
    else:
        if area2 > area1:
            return "El rectángulo 2 tiene un área mayor que el rectángulo 1"
        if area1 == area2:
            return "El área de ambos rectángulos es igual"


# Función principal: Lee las bases y alturas y llama a las otras funciones para calcular e imprimir los resultados.
def main():
    base1 = int(input("Introduzca la base del primer rectángulo: "))
    altura1 = int(input("Introduzca la altura del primer rectángulo: "))
    base2 = int(input("Introduzca la base del segundo rectángulo: "))
    altura2 = int(input("Introduzca la altura del segundo rectángulo: "))
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)
    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    areaMayor = sacarMayor(area1, area2)
    print("El área del rectángulo 1 es: %d y su perímetro es: %d" % (area1, perimetro1))
    print("El Área del rectángulo 2 es: %d y su perímetro es: %d" %  (area2, perimetro2))
    print(areaMayor)

main()