#Autor Daniel Cordova Bermudez
#Grupo 02
#Descripcion: El programa determina el tipo de triangulo con los datos de los lados.


#Funacion tipoTriangulo compara la información de los lados para ver si es correcta, en ese caso ve que tipo de triangulo es según los ángulos-

def tipoTriangulo(a, b, c):


    if (a > 0) and (b > 0) and (c > 0):

        if a == b == c:
            return "Los lados corresponden a un triángulo equilatero"
        if  c != a != b != c:
            return "Los lados corresponden a un triángulo rectangúlo"
        if a == b != c or a != b == c or b != c == a:
            return "Los lados corresponden a un triángulo isósceles"


    else:

        return "Estos lados no corresponden a un triángulo"


#Función principal que pide los datos e los lados e imprime el resultado del tipo de triangulo.
    
def main():

    lado1 = int(input("Primer lado del triangulo:  "))
    lado2 = int(input("Segundo lado del triangulo: "))
    lado3 = int(input("Tercer lado del triangulo: "))

    resultado = tipoTriangulo(lado1,lado2,lado3)
    print(resultado)

main()
