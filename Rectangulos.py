# Autor: Luis Armando Miranda Alcocer
# Descripción: Calcula el área y perímetro de dos rectángulos, dadas sus dimensiones.

def calcularAreaUno(baseUno, alturaUno): #Multiplicar base por altura para sacar el área
    areaUno = baseUno * alturaUno
    return areaUno


def calcularPerimetroUno (baseUno, alturaUno): #Sumar el doble de la base más el doble de la altura para sacar el perímetro
    perimetroUno = (2*baseUno)+(2*alturaUno)
    return perimetroUno


def calcularAreaDos (baseDos, alturaDos): #Multiplicar base por altura para sacar el área del segundo rectángulo
    areaDos = baseDos * alturaDos
    return areaDos


def calcularPerimetroDos (baseDos, alturaDos): #Sumar el doble de la base más el doble de la altura para sacar el perímetro
    perimetroDos = (2*baseDos)+(2*alturaDos)
    return perimetroDos


def main():
    baseUno = int(input("Inserta la base del primer rectángulo: ")) #Se introducen los datos
    alturaUno = int(input("Inserta la altura del primer rectángulo: "))

    baseDos = int(input("Inserta la base del segundo rectángulo: "))
    alturaDos = int(input("Inserta la altura del segundo rectángulo: "))
    print(" _________________________________________________")
    print("  ")

    areaUno = calcularAreaUno (baseUno, alturaUno) #Llamar a la función para calcular el área del primer rectángulo
    print ("El área del primer rectángulo es: ", areaUno)

    perimetroUno = calcularPerimetroUno (baseUno, alturaUno) #Llamar a la función para calcular el perímetro del primer rectángulo
    print("El perímetro del primer rectángulo es: ", perimetroUno)
    print ("  ") #Espacio

    areaDos = calcularAreaDos(baseDos, alturaDos)  # Llamar a la función para calcular el área del segundo rectángulo
    print("El área del segundo rectángulo es: ", areaDos)

    perimetroDos = calcularPerimetroDos(baseDos,alturaDos)  # Llamar a la función para calcular el perímetro del segundo rectángulo
    print("El perímetro del segundo rectángulo es: ", perimetroDos)
    print ("   ") # Espacio

    if areaUno > areaDos: #Determinar si el primer rectángulo tiene mayor área
        print ("El primer rectángulo tiene mayor área")

    if areaUno < areaDos: #Determinar si el segundo rectángulo tiene mayor área
        print ("El segundo rectángulo tiene mayor área")

    if areaUno == areaDos: #Determinar si el primer rectángulo tiene la misma área que el segundo
        print ("Ambos rectángulos tienen la misma área")

main()