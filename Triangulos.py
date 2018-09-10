#Autor: Saúl Figueroa Conde
#Matrícula: A01747306
#Grupo: 02
#Este programa recibe los 3 valores, correspondientes a los lados de un triángulo, dados por el usuario y determina
#el tipo de triángulo al que corresponden dichos valores.
#---------------------------------------------------------------------------------------------------------------------


#Se importa la biblioteca math, esta se utilizará en la función clasificarTriangulo para determinar si el triángulo
#es rectángulo.
import math

#Se declara la función clasificarTriangulo. Recibe como parámetros ladoA, ladoB y ladoC. La función determina
#si los valores dados por el usuario corresponden a un triángulo y, en caso de que sí, determina el tipo de triángulo
#que corresponde según las medidas dadas. Al final, la función regresa el tipo de triángulo (en formato string).
def clasificarTriangulo(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        print("Estos lados no corresponde a un triángulo")
        main()

    elif a == b and b == c:
        return "equilátero"

    elif c == math.sqrt((a**2) + (b**2)) or a == math.sqrt((c**2) + (b**2)) or b == math.sqrt((a**2) + (c**2)) :
        return "rectángulo"

    elif (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        return "isósceles"

    else:
        return "escaleno"


#Se declara la función main. Primero se le pregunta al usuario los valores de los lados A, B y C. Estos valores se
#envían a la función clasificarTriangulo. Una vez que la función clasificarTriangulo regrese el valor de triangulo,
#se imprime el resultado (valor de la variable triangulo).
def main():
    ladoA = float(input("Indique el valor del lado A:" ))
    ladoB = float(input("Indique el valor del lado B:"))
    ladoC = float(input("Indique el valor del lado C:"))

    triangulo = clasificarTriangulo(ladoA, ladoB, ladoC)

    print("")
    print("El tipo de triángulo, según las medidas que ha especificado, es:", triangulo)

    print("")
    salir = input(("Muchas gracias por haber usado el programa."))
    quit()


#Se llama a la función main. Así corre cada una de las funciones desempeñando la tarea designada para dar solución
#a la problemática planteada.
main()