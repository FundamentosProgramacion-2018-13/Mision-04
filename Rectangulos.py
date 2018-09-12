# Alex Serrano Durán
# Este programa calcula el perímetro y área de dos rectángulos y también indica la mayor área.


def calcularPerimetro(base, altura):        # La función regresa el perímetro a partir de los lados
    perimetro = base*2 + altura*2
    return perimetro


def calcularArea(base, altura):             # La función regresa el área según los lados
    area = base * altura
    return area


def main():                                 # La función lee los inputs del usuario, imprime resultados y el área mayor.
    base1 = int(input("Teclea la base del primer rectángulo: "))
    altura1 = int(input("Teclea el altura del primer rectángulo: "))
    base2 = int(input("Teclea la base del segundo rectángulo: "))
    altura2 = int(input("Teclea el altura del segundo rectángulo: "))

    perimetroUno = calcularPerimetro(base1, altura1)
    perimetroDos = calcularPerimetro(base2, altura2)
    AreaUno = calcularArea(base1, altura1)
    AreaDos = calcularArea(base2, altura2)

    print('''
Primer rectángulo:
    Perímetro: %.1f u
    Área: %.1f u²
Segundo rectángulo:
    Perímetro: %.1f u
    Área: %.1f u²''' % (perimetroUno, AreaUno, perimetroDos, AreaDos))

    if AreaUno > AreaDos:
        print("El área del primer rectángulo es mayor.")
    if AreaDos > AreaUno:
        print("El área del segundo rectángulo es mayor.")
    if AreaDos == AreaUno:
        print("Las áreas son iguales.")


main()
