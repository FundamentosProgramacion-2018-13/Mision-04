#Autor: Marco González Elizalde
#Calcula las áreas y perimetros de dos rectangulos e indica el de mayor area


#Calcula el area de un rectangulo dados el largo y el ancho
def calcularArea(largo, ancho):
    area = largo * ancho
    return area


#Calcula el perimetro de un rectangulo dados el largo y el ancho
def calcularPerimetro(largo, ancho):
    perimetro = 2 * (largo + ancho)
    return perimetro


#Compara el area de dos rectángulos y regresa un string definiendo el mayor
def compararArea(areaA, areaB):
    if(areaA > areaB):
        return "El primer rectángulo tiene un área mayor"

    if(areaB > areaA):
        return "El segundo rectángulo tiene un área mayor"

    return("Ambos rectángulos tienen la misma área")


#Funcion principal
def main():

    largoA = int(input("Ingresa el largo del primer rectangulo: "))
    anchoA = int(input("Ingresa el ancho del primer rectangulo: "))
    print("")
    largoB = int(input("Ingresa el largo del segundo rectangulo: "))
    anchoB = int(input("Ingresa el largo del segundo rectangulo: "))

    areaA = calcularArea(largoA, anchoA)
    perimetroA = calcularPerimetro(largoA, anchoA)

    areaB = calcularArea(largoB, anchoB)
    perimetroB = calcularPerimetro(largoB, anchoB)

    areaMayor = compararArea(areaA, areaB)

    print("""
Área del primer rectángulo: %.02f
Perímetro del primer rectángulo: %.02f
    
Área del segundo rectangulo: %.02f
Perímetro del segundo rectángulo: %.02f
    
%s
    """ %(areaA, perimetroA, areaB, perimetroB, areaMayor))


#Corre el programa principal
main()
