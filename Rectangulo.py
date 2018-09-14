# Autor: Danhel Alejandro Mercado Velasco
# Este programa se encarga de calcular el area y perimetro de dos rectangulos

# Esta función calcula el area
def calculararea(ancho, largo):
    area = ancho*largo
    return area


# Esta función se encarga de calcular el perimetro
def calcularperimetro(ancho, largo):
    perimetro = (ancho * 2) + (largo * 2)
    return perimetro


# Esta función se encarga de saber cual de las dos areas es mayor
def calcularmayor(area1, area2):
    if area1 == area2:
        return "El area de ambos rectangulos son iguales"
    if area1 > area2:
        return "Area del rectangulo 1 es mayor a la del Area 2"
    else:
        return "Area del rectangulo 1 es mayor a la del Area 2"


# Esta funcion se encarga de leer datos, calcular variables e imprimirlos
def main():
    anRectangulo1 = float(input("Escribe el ancho del primer rectangulo:" ))
    laRectangulo1 = float(input("Escribe el largo del primer rectangulo:" ))
    anRectangulo2 = float(input("Escribe el ancho del segundo rectangulo:" ))
    laRectangulo2 = float(input("Escribe el largo del segundo rectangulo:" ))
    area1 = calculararea(anRectangulo1, laRectangulo1)
    area2 = calculararea(anRectangulo2, laRectangulo2)
    perimetro1 = calcularperimetro(anRectangulo1, laRectangulo1)
    perimetro2 = calcularperimetro(anRectangulo2, laRectangulo2)
    mayor = calcularmayor(area1, area2)
    print("Area del primer rectangulo: %d" % area1)
    print("Perimetro del primer rectangulo: %d" % perimetro1)
    print("Area del primer rectangulo: %d" % area2)
    print("Perimetro del primer rectangulo: %d" % perimetro2)
# Llamada a la función
main()