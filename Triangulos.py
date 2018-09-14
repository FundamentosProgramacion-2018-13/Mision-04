# Autor: Luis Humberto Burgueño Paz
# Lee los lados de un triángulo e indica si es un triángulo equilátero, isóceles o escaleno y verifica si es un triángulo rectángulo.


#Recibe los lados y verifica si es un triángulo rectángulo
def verificarTriangulo(lado1, lado2, lado3):
    if lado1 == ((lado2**2) + (lado3**2))**0.5:
        return "es un triángulo rectángulo"
    else:
        if lado2 == ((lado1 ** 2) + (lado3 ** 2)) ** 0.5:
            return "es un triángulo rectángulo"
        if lado3 == ((lado2 ** 2) + (lado1 ** 2)) ** 0.5:
            return "es un triángulo rectángulo"
        else:
            return "no es un triángulo rectángulo"


#Recibe los lados y regresa el tipo de triángulo
def determinarTipo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "es un triángulo equilátero"
    else:
        if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            return "es un triángulo escaleno"
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "es un triángulo isóceles"


#Función Principal: Lee los lados y llama a las otras funciones para mostrar los resultados
def main():
    lado1 = int(input("Introduce el valor del lado 1: "))
    lado2 = int(input("Introduce el valor del lado 2: "))
    lado3 = int(input("Introduce el valor del lado 3: "))
    if lado1 <= 0:
        print("Estos lados no corresponden a un triángulo")
    else:
        if lado2 <= 0:
            print("Estos lados no corresponden a un triángulo")
        if lado3 <= 0:
            print("Estos lados no corresponden a un triángulo")
        else:
            rectanguloTriangulo = verificarTriangulo(lado1, lado2, lado3)
            tipoTriangulo = determinarTipo(lado1, lado2, lado3)
            print("Este %s y %s" % (tipoTriangulo, rectanguloTriangulo))


main()