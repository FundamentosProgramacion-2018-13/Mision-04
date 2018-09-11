# Autor: Rubén Villalpando Bremont
# El programa recibe 3 lados de un triángulo e indica el tipo de triángulo que es si es que existe, si los lados no
# corresponden a un triángulo el programa te lo notifica


# La función te dice el tipo de triángulo que es a partir de los lados
def calcularTipoDeTriangulo(ladoUno, ladoDos, ladoTres):
    if ladoDos == ladoTres and ladoTres == ladoUno:
        return "El triángulo es equilátero"
    elif (ladoUno == ladoDos and ladoUno != ladoTres) or (ladoUno == ladoTres and ladoTres != ladoDos) or (ladoTres == ladoDos and ladoDos != ladoUno):
        return "El triángulo es isósceles"
    elif ladoUno**2 + ladoDos**2 == ladoTres**2 or ladoUno**2 + ladoTres**2 == ladoDos**2 or ladoTres**2 + ladoDos**2 == ladoUno**2:
        return "El triángulo es rectángulo"
    else:
        return "El triángulo no se puede clasificar"


# Función principal
def main():
    ladoUno = int(input("Escribe el tamaño del primer lado del triángulo: "))
    ladoDos = int(input("Escribe el tamaño del segundo lado del triángulo: "))
    ladoTres = int(input("Escribe el tamaño del tercer lado del triángulo: "))
    if ladoUno + ladoDos > ladoTres or ladoUno + ladoTres > ladoDos or ladoTres + ladoDos > ladoUno:
        print(calcularTipoDeTriangulo(ladoUno, ladoDos, ladoTres))
    else:
        print("Estos lados no corresponden a un triángulo")

# Llamar a main
main()