# Sebastian Macias - A01376492
# Verificar el tipo de triangulos basándose en los lados


# Calcular el tipo de triangulo que se presenta
def calcularTipoTriangulo(lado1, lado2, lado3):
    if lado1 != lado2 != lado3:
        return "rectángulo"
    else:
        if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "isósceles"
        else:
            if lado1 == lado2 == lado3:
                return "equilatero"


# Encontrar el lado más grande
def buscarMayor3(valorA, valorB, valorC):
    if valorA > valorB and valorA > valorC:
        return valorA
    if valorB > valorA and valorB > valorC:
        return valorB
    return valorC


# Calcular la suma de los lados pequeños
def calcularSumaLadosMenores(lado1, lado2, lado3, ladoMayor):
    if ladoMayor == lado1:
        return lado2 + lado3
    else:
        if ladoMayor == lado2:
            return lado1 + lado3
        else:
            if ladoMayor == lado3:
                return lado1 + lado2


# Determinar si los lados dados es un triángulo existente por medio de una comparación
def calcularEsTriangulo(sumaLadosMenores, ladoMayor):
    if ladoMayor >= sumaLadosMenores:
        return "No es triángulo"
    else:
        return "Es un triangulo"


# Decir si es un triángulo, en dado caso que lo sea mencional el tipo de triángulo que es.
def main():
    lado1 = int(input("Escribe el valor del lado: "))
    lado2 = int(input("Escribe el valor del lado: "))
    lado3 = int(input("Escribe el valor del lado: "))

    ladoMayor = buscarMayor3(lado1, lado2, lado3)
    sumaLadosMenores = calcularSumaLadosMenores(lado1, lado2, lado3, ladoMayor)
    esTriangulo = calcularEsTriangulo(sumaLadosMenores, ladoMayor)

    if esTriangulo == "Es un triangulo":
        tipoDeTriangulo = calcularTipoTriangulo(lado1, lado2, lado3)
        print("")
        print("Es un triángulo ", tipoDeTriangulo)
    else:
        print("")
        print("Estos lados no corresponden a un triángulo")


main()
