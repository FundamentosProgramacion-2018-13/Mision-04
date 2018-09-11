#Autor Daniel Cordova Bermudez
#Grupo 02
#Descripcion:


def calcularArea(ancho, largo):

    area=ancho*largo
    return area


def calcularPerimetro(ancho, largo):

    perimetro=ancho*2+largo*2
    return perimetro

    pass


def calcularMayor(area1, area2):

    if area1 == area2:
        return "El area de ambos rectangulos son iguales"
    else:
        if area1 > area2:
            return "Area del rectangulo 1 es mayor a la del Area 2"
        else:
            return "Area del rectangulo 1 es mayor a la del Area 2"


    pass


def main():

    anchoRectangulo1 = float(input("Escribe el ancho del primer rectangulo:"))
    largoRectangulo1 = float(input("Escribe el largo del primer rectangulo:"))
    anchoRectangulo2 = float(input("Escribe el ancho del segundo rectangulo:"))
    largoRectangulo2 = float(input("Escribe el largo del segundo rectangulo:"))

    area1 = calcularArea(anchoRectangulo1,largoRectangulo1)
    area2 = calcularArea(anchoRectangulo2,largoRectangulo2)

    perimetro1 = calcularPerimetro(anchoRectangulo1,largoRectangulo1)
    perimetro2 = calcularPerimetro(anchoRectangulo2, largoRectangulo2)

    mayor= calcularMayor(area1,area2)


    print("""
    
    Area del primer rectangulo: %d
    Perimetro del primer rectangulo: %d
    Area del primer rectangulo: %d 
    Perimetro del primer rectangulo: %d
    
    %s
    """ % (area1,perimetro1,area2,perimetro2,mayor))



main()


