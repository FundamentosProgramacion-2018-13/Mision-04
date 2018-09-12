# Luis Jonathan Rosas Ramos
# A01377942
# Calcular el area y perimetro de dos triangulos, para despues comprar sus datos eh indicar si uno es mayor
# que otro o son iguales

#Funcion para calcular el perimetro
def calcularPerimetro(b,h):
    perimetro = (2*b+2*h)  #Usamos una formula donde 2 veces la base mas 2 veces la altura da el perimetro
    return perimetro


#Funcion para calcular el area
def calcularArea(b,h):
    area = b*h      #Usamos la formula para las figuras donde base por altura de el area
    return area


# Definir funcion principal
def main():
    baseUno = int(input("Indica la base: "))
    alturaUno = int(input("Indica la altura: "))
    baseDos = int(input("Ingresa la base del rectangulo dos: "))
    alturaDos = int(input("Indica la altura del triangulo dos: "))
    perimetroUno = calcularPerimetro(baseUno,alturaUno)
    perimetroDos = calcularPerimetro(baseDos, alturaDos)
    areaUno = calcularArea(baseUno, alturaUno)
    areaDos = calcularArea(baseDos,alturaDos)
    print("Perimetro uno es: ",perimetroUno," Area uno es:", areaUno)
    print("Perimetro dos es: ", perimetroDos, " Area dos es:", areaDos)
    #Comparar las areas si la uno es mayor que la dos
    if areaUno > areaDos:
        print("Cuadrado uno es mas grande")
    #comparar las areas si dos es mayor que uno
    elif areaUno < areaDos:
        print("Cuadrado dos es mas grande")
    # condicion para el caso faltante
    else:
        print("Las areas son iguales")


main()