# AUTOR: Zoe Caballero Dominguez
# El siguiente programa calcula el perímetro y área de dos rectángulos para luego comparar cuál es el de mayor área

#Esta función calcula el perímetro del rectángulo con los datos de largo y ancho y regresa el resultado a main
def calcularPerimetro(largo, ancho):
    perimetro = (2* largo) + (2*ancho)
    return perimetro


#Esta funcion calcula el área del rectángulo con el largo y el ancho. Regresa el resultado a main
def calcularArea(largo, ancho):
    area = largo * ancho
    return area


#Función principal
def main():
    largoPrimerRectangulo = int(input("Escribe el largo del primer rectángulo: "))
    anchoPrimerRectangulo = int(input("Escribe el ancho del primer rectángulo: "))
    largoSegundoRectangulo = int(input("Escribe el largo del segundo rectángulo: "))
    anchoSegundoRectangulo = int(input("Escribe el ancho del segundo rectángulo: "))

    perimetroPrimerRectangulo = calcularPerimetro(largoPrimerRectangulo, anchoPrimerRectangulo)
    perimetroSegundoRectangulo = calcularPerimetro(largoSegundoRectangulo, anchoSegundoRectangulo)

    areaPrimerRectangulo = calcularArea(largoPrimerRectangulo, anchoPrimerRectangulo)
    areaSegundoRectangulo = calcularArea(largoSegundoRectangulo, anchoSegundoRectangulo)

    print("--------------------------------------------------")
    print("El perímetro del primer rectángulo es: %0.2f cm" % (perimetroPrimerRectangulo))
    print("El perímetro del segundo rectángulo es: %0.2f cm" % (perimetroSegundoRectangulo))
    print("")
    print("El área del primer rectángulo es: %0.2f cm2" % (areaPrimerRectangulo))
    print("El área del segundo rectángulo es: %0.2f cm2" % (areaSegundoRectangulo))
    print("")

    if areaPrimerRectangulo == areaSegundoRectangulo:
        print ("Las áreas de los dos rectángulos son iguales")
    else:
        if areaPrimerRectangulo > areaSegundoRectangulo:
            print ("El área del primer rectángulo es mayor que la del segundo")
        else:
            print ("El área del segundo rectangulo es mayor que la del primero")


#Llama a la función
main()