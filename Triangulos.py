#Nombre Diego Armando Ayala Hernández

#Matrícula A01376727

#resumen del programa: Pide los lados de dos rectangulos y define que tipo de triangulo son

# Te dice si un triángulo es equilátero, isóceles  o rectángulo de acuerdo a sus longitudes
def definirTriangulo(ladoUno,ladoDos, ladoTres):
    if ladoDos == ladoUno and ladoUno ==ladoTres:
        return "Equilátero"
    elif ladoUno == ladoDos or ladoDos == ladoTres or ladoUno == ladoTres:
        return "Isóceles"
    elif ladoUno**2 == ladoDos**2 + ladoTres**2 or ladoDos**2 == ladoUno**2 + ladoTres**2 or ladoTres**2 == ladoUno**2 + ladoDos**2:
        return " Rectángulo"
    else: return "Estos lados no corresponden a un triángulo"


#pide los lados de los triangulos y los imprime
def main():
    ladoUno =int(input("Lado 1 del Primer triángulo : "))
    ladoDos =int(input("Lado 2 del Primer triángulo : "))
    ladoTres =int(input("Lado 3 del Primer triángulo : "))
    LadoUnoTrianguloDos=int(input("Lado 1 del Segundo Triangulo:"))
    LadoDosTrianguloDos=int(input("Lado 2 del Segundo Triangulo:"))
    LadoTresTrianguloDos=int(input("Lado 3 del Segundo Triangulo:"))
    definirtriangulouno=definirTriangulo(ladoUno, ladoDos, ladoTres)
    definirtriangulodos=definirTriangulo(LadoUnoTrianguloDos, LadoDosTrianguloDos, LadoTresTrianguloDos)
    print("El primer triangulo es : ", (definirtriangulouno))
    print("El segundo triangulo es : " , (definirtriangulodos))
main()
