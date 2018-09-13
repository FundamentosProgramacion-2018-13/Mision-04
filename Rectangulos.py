# Autor: Carlos Alberto Reyes Ortiz
# Resuelve el área y perímetro de dos rectángulos dado sus dimensiones.
# También te dice que área es mayor o si son iguales



def calcularArea(altura, ancho):    #Calcula el área de un rectángulo
    area = altura * ancho
    return area



def calcularPerimetro(altura, ancho):   #Calcula el perímetro de un rectángulo
    perimetro = (2 * altura) + (2 * ancho)
    return perimetro



def decirCualMayorArea(areaUno,areaDos):  #Te dice cual de las dos áreas es mayor o si son iguales
    if areaUno > areaDos:
        return "El área del primer rectángulo es mayor"
    elif areaUno < areaDos:
            return "El área del segundo rectángulo es mayor"
    return "Las áreas son iguales"




def main():  #Función principal: Dada sus dimensiones,
             # te da el área y perímetro de los dos rectángulos. También te dice cual área es mayor o si son iguales
    print("Escribe las dimensiones del primer rectángulo")
    alturaUno = float(input("Altura: "))
    anchoUno = float(input("Ancho: "))
    print()
    print("Escribe las dimensiones del segundo rectángulo")
    alturaDos = float(input("Altura: "))
    anchoDos = float(input("Ancho: "))

    perimetroUno = calcularPerimetro(alturaUno, anchoUno)
    perimetroDos = calcularPerimetro(alturaDos, anchoDos)
    areaUno = calcularArea(alturaUno, anchoUno)
    areaDos = calcularArea(alturaDos, anchoDos)

    print()
    print("-----------------------")
    print()
    print("Primer rectángulo")
    print("El área es: ", (areaUno)) # Nota personal: la coma se usa con parametros,
    #  es decir cuando cambias la variable de la función que llamaste
    print("El perímetro es: ", (perimetroUno))
    print()
    print("Segundo rectángulo")
    print("El área es: ", (areaDos))
    print("El perímetro es: ", (perimetroDos))
    print()

    mayorArea = decirCualMayorArea(areaUno, areaDos)
    print(mayorArea)




#Llamar función
main()