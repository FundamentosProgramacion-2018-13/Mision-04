#Autor: Saúl Figueroa Conde
#Matrícula: A01747306
#Grupo: 02
#Este programa lee las dimensiones de dos rectángulos, calcula e imprime el perímetro y el área de cada uno.
#---------------------------------------------------------------------------------------------------------------------

#Se declara la función determinarMayor:
#Esta función recibe como parámetros el área de ambos rectángulos y las compara para ver cuál es el de mayor área o
#si tienen valores iguales. Regresa el valor del área mayor.
def determinarMayor(rectangulo1, rectangulo2):
    if rectangulo1 > rectangulo2:
        return "el rectangulo 1"
    elif rectangulo1 == rectangulo2:
        return "ninguno... resulta que tienen la misma área."
    return "el rectangulo 2"


#Se declara la función calcularPerimetro:
#Esta función recibe como parámetros la base y la altura de los dos rectángulos y regresa el valor del perímetro.
def calcularPerimetro(b, h):

    perimetro = (b * 2) + (h * 2)
    return perimetro


#Se declara la función calcularArea:
#Esta función recibe como parámetros la base y la altura de los dos rectángulos y regresa el valor del área.
def calcularArea(b, h):

    area = b * h
    return area


#Se declara la función main. Se hace uso de dos listas que almacenan los valores
#del área y el perímetro de cada rectángulo. El valor de base y altura se envía a las funciones calcularArea y
#calcularPerimetro. Una vez calculado los valores del área, estos se envían a la función determinarMayor.
#Aquí se regresa cada valor que calculan las otras funciones y se imprimen.
#En otras palabras, la función main se encarga del input y el output del programa.
def main():

    rectangulo1 = []
    rectangulo2 = []

    base = float(input("Escriba la base del primer rectángulo: "))
    altura = float(input("Escriba la altura del primer rectángulo: "))

    area = calcularArea(base, altura)
    perimetro = calcularPerimetro(base, altura)

    rectangulo1.append(area)
    rectangulo1.append(perimetro)

    base = float(input("Escriba la base del segundo rectángulo: "))
    altura = float(input("Escriba la altura del segundo rectángulo: "))

    area = calcularArea(base, altura)
    perimetro = calcularPerimetro(base, altura)

    rectangulo2.append(area)
    rectangulo2.append(perimetro)

    print("")
    print("El área del primer rectángulo  es {} y su perímetro {}" .format(rectangulo1[0], rectangulo1[1]))
    print("El área del segundo rectángulo  es {} y su perímetro {}".format(rectangulo2[0], rectangulo2[1]))

    mayor = determinarMayor(rectangulo1[0], rectangulo2[0])

    print("")
    print("El rectángulo con mayor área es: ", mayor)

    print("")
    salir = input("Gracias por haber usado este programa.")
    quit()


#Se llama a la función main y comienza a ejecutarse el programa que resolverá la problemática planteada.
main()