#Autor: David Alejandro Nicolás Palos
#Descripción: Calcula el area y perimetro de dos rectangulos con medidas dadas por el usuario del ancho y alto


def calcularPerimetroRectanguloUno(anchoPrimerRectangulo,altoPrimerRectangulo): #Calcula el perimetro del primer rectangulo

    perimetro1 = (anchoPrimerRectangulo*2)+(altoPrimerRectangulo*2)
    return perimetro1


def calcularPerimetroRectanguloDos(anchoSegundoRectangulo, altoSegundoRectangulo): #Calcula el perimetro del segundo rectangulo

    perimetro2 = (anchoSegundoRectangulo*2)+(altoSegundoRectangulo*2)
    return(perimetro2)


def calcularAreaRectanguloUno(anchoPrimerRectangulo, altoPrimerRectangulo): #Calcula el area del primer rectangulo

    area1 = anchoPrimerRectangulo * altoPrimerRectangulo
    return area1


def calcularAreaRectanguloDos(anchoSegundoRectangulo, altoSegundoRectangulo): #Calcula el area del segundo rectangulo

    area2 = anchoSegundoRectangulo * altoSegundoRectangulo
    return area2


def compararAreas(area1,area2): #Compara las areas de ambos rectangulos y define cual es mayor o si son iguales

    if area1 > area2:
        return"El area del rectangulo 1 es mayor"
    else:
        if area2 > area1:
            return "El area del rectangulo 2 es mayor"
        else:
            return "El area de los rectangulos es igual"


def main(): #Funcion main, lee e imprime resultados

    anchoPrimerRectangulo = float(input("Escribe el ancho del rectangulo 1: "))
    altoPrimerRectangulo = float(input("Escribe el alto del rectangulo 1: "))
    anchoSegundoRectangulo = float(input("Escribe el ancho del rectangulo 2: "))
    altoSegundoRectangulo = float(input("Escribe el alto del Rectangulo 2: "))

    area1 = calcularAreaRectanguloUno(anchoPrimerRectangulo,altoPrimerRectangulo)
    area2 = calcularAreaRectanguloDos(anchoSegundoRectangulo,altoSegundoRectangulo)

    print("")
    print("El perímetro del rectangulo 1 es:",calcularPerimetroRectanguloUno(anchoPrimerRectangulo,altoPrimerRectangulo))
    print("El perímetro del rectangulo 2 es:", calcularPerimetroRectanguloDos(anchoSegundoRectangulo,altoSegundoRectangulo))
    print("")
    print("El area del rectangulo 1 es:", calcularAreaRectanguloUno(anchoPrimerRectangulo,altoPrimerRectangulo))
    print("El area del rectangulo 2 es:", calcularAreaRectanguloDos(anchoSegundoRectangulo,altoSegundoRectangulo))
    print("")
    print(compararAreas(area1, area2))

main()