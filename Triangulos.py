#Autor Claudio Mayoral García
#Descripción Dice que tipo de triángulo es dependiendo de los valores que se les asignen a los lados
#Y si no cumple con las características del triángulo manda un mensaje de error


#Esta función regresa el tipo de triángulo que es pero si no es un triángulo regresa un anuncio de error
def esTriangulo(numero, numero2, numero3):
    if numero <= 0 or numero2 <= 0 or numero3 <= 0:
        return "El triángulo no existe"
    if (numero + numero2) <= numero3 or (numero + numero3) <= numero2 or (numero3 + numero2) <= numero:
        return "El triángulo no existe"
    elif numero**2 + numero2**2 == numero3**2 or numero**2 + numero3**2 == numero2**2 or numero2**2 + numero3**2 == numero**2:
        return "Es un triángulo rectangulo"
    elif numero == numero2 == numero3:
        return "Es un triángulo equilatero"
    elif numero == numero2 or numero ==numero3 or numero2 == numero3:
        return "Es un triángulo isóceles"
    else:
    return "Es un triángulo escaleno"


#Función principal, pide valores de los lados del triángulo y manda a imprimir que tipo de triángulo es o si no existe
def main():
    numero = int(input("Número: "))
    numero2 = int(input("Número: "))
    numero3 = int(input("Numero: "))

    tipoTriangulo= esTriangulo(numero, numero2, numero3)
    print(tipoTriangulo)


#Llama a la función principal
main()
