#Joshua Sánchez Martínez A01274269
#Define de que triangulo se trata según los datos ingresados

#Definde el tipo de triangulo
def definirTipoDeTriangulo(lado1,lado2,lado3):


    if lado1 == lado2 and lado2== lado3:
        return "Equilátero"
    else:
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Isósceles"
        else:
            if lado1 != lado2 and lado2 != lado3:
                return "Rectángulo"


#Función principal
def main ():
    lado1 = int(input("Teclea la primer medida del triangulo: "))
    lado2 = int(input("Teclea la segunda medida del triangulo: "))
    lado3 = int(input("Teclea la tercer medida del triangulo: "))

    if lado1 >0 and lado2 > 0 and lado3 > 0:
        tipoDeTriangulo = definirTipoDeTriangulo(lado1, lado2, lado3)
        print("Se trata de un triángulo: ", tipoDeTriangulo)
    else:
        print("Estos lados no corresponden a un triángulo")


#Llamar a la función main
main()