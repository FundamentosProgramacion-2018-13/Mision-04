#Autor: Víctor Manuel Rodríguez Loyola
#Este programa lee el valor de los lados de un triàngulo y determina què tipo de triàngulo es


def CompararLados(lado1, lado2, lado3): #Determina qué tipo de triángulo es mediante la comparación de sus lados
    if lado1 == lado2 and lado1==lado3:
        return 'Equilàtero'

    if lado1== ((lado2**2)+(lado3**2))**0.5:
        return 'Rectangulo'
    else:
        if lado2== ((lado1**2)+(lado3**2))**0.5:
            return 'Rectangulo'
        else:
            if lado3== ((lado1**2)+(lado2**2))**0.5:
                return 'Rectangulo'


    if lado1==lado2 and lado1 != lado3:
        return 'Isósceles'
    else:
        if lado1==lado3 and lado1!= lado2:
            return 'Isósceles'
        else:
            if lado2== lado3 and lado2 !=lado1:
                return 'Isósceles'

    return 'Estos lados no corresponden a un triángulo'


def main():
    ladoUno=int(input("Teclea el valor del primer lado: "))
    ladoDos= int(input("Teclea el valor del segundo lado: "))
    ladoTres= int(input("Teclea el valor del tercer lado: "))
    tipoDeTriangulo= CompararLados(ladoUno, ladoDos, ladoTres)
    if ladoTres and ladoDos and ladoUno <0:
        print("Error. Inténtalo de nuevo.")
    else:
        print("Este triángulo es ",tipoDeTriangulo)


main()