# Autor: Humberto Carrillo Gómez
# Descripción: Este programa determina el tipo de triángulo (Rectángulo, Isósceles, equilátero)

# Calcula el tipo de triángulo en base a los lados.
def calcularTipo(ladoA,ladoB,ladoC):

    tipo = 0
    if ladoA == ladoB == ladoC:
        tipo="Equilátero"

    elif ladoA == ladoB and ladoA != ladoC or ladoA==ladoC and ladoA != ladoB or ladoB==ladoC and ladoB!=ladoA:
        tipo= "Isósceles"

    elif (ladoA)**2 + (ladoB)**2 == (ladoC)**2 or (ladoB)**2 + (ladoC)**2==(ladoA)**2 or (ladoC)**2 + (ladoA)**2==(ladoB)**2:
        tipo= "Rectángulo"

    return tipo


# Función principal: resuelve el problema.
def main():
    ladoA = float(input("Teclea la longitud del lado A: "))
    ladoB = float(input("Teclea la longitud del lado B: "))
    ladoC = float(input("Teclea la longitu""d del lado C: "))

    tipo = calcularTipo(ladoA,ladoB,ladoC)

    if ladoA <= 0 or ladoB <= 0 or ladoC <= 0:
        print("Estos lados no corresponden a un triángulo")

    else:
        print("El triángulo es: ", tipo)


# Llamado a la función principal
main()