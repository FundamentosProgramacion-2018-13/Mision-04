# Autor: Luis Armando Miranda Alcocer
# Descripción: Acorde a los lados de un triángulo, se determina si es isósceles, equilátero o rectándulo

def calcularTriangulo(ladoUno, ladoDos, ladoTres): #Se comparan los lados para determinar el tipo de triangulo
    if ladoUno == ladoDos == ladoTres: #Los equilateros tienen sus tres lados iguales
        triangulo = ("Equilatero")
        return triangulo

    if ladoUno == ladoDos != ladoTres or ladoUno == ladoTres != ladoDos or ladoTres == ladoDos != ladoUno: #Los isósceles tienen dos lados iguales y uno diferente
        triangulo = ("Isósceles")
        return triangulo

    if (ladoUno ** 2) == (ladoDos ** 2) + (ladoTres ** 2) or (ladoDos ** 2) == (ladoTres ** 2) + (ladoUno ** 2) or (
            ladoTres ** 2) == (ladoUno ** 2) + (ladoDos ** 2): #Los triángulos rectángulos cumplen con el teorema de pitágoras.
        triangulo= ("Rectángulo")
        return triangulo

def main ():
    ladoUno = int(input("Ingrese un lado del triángulo: ")) #Se leen los lados
    ladoDos = int(input("Ingrese un lado del triángulo: "))
    ladoTres = int(input("Ingrese un lado del triángulo: "))

    if ladoUno <= 0 or ladoDos <= 0 or ladoTres <= 0: #Si no contiene errores, pasa a ser clasificado
        print ("Estos lados no corresponden a un triángulo")
    else:
        triangulo= calcularTriangulo(ladoUno, ladoDos, ladoTres)
        print ("Es :", triangulo)


main()