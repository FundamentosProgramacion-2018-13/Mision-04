#Autor Daniel Cordova Bermudez
#Grupo 02
#Descripcion:El programa calcula el area junto con el perimetro de dos rectangulos, al final compara cual de los dos es mayor.


#Función calcularArea se encarga de calcular el area de los rectangulos con la información previa.

def calcularArea(ancho, largo):

    area=ancho*largo
    return area


#Funcion calcularPerimetro se encarga de calcular el perimetro de los rectangulos.

def calcularPerimetro(ancho, largo):

    perimetro=ancho*2+largo*2
    return perimetro


#Función calcularMayor se encarga de ver que area es mayor con una serie de condicionales.

def calcularMayor(area1, area2):

    if area1 == area2:
        return "El area de ambos rectangulos son iguales"
    else:
        if area1 > area2:
            return "Area del rectangulo 1 es mayor a la del Area 2"
        else:
            return "Area del rectangulo 1 es mayor a la del Area 2"

 
#Funcion principal que se encarga de pedir datos, enviarlos a otras funciones e imprime los resultaods finales.

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


