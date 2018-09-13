#Autor: Samantha Martínez Franco A01747686
#Calcular area y perímetro de dos rectangulos

#función que calcula area
def calcularArea(altura,ancho):
    area=altura*ancho
    return area


#función que calcula perímetro
def calcularPerímetro(altura,ancho):
    perimetro=2*altura+2*ancho
    return perimetro


#función principal
def main():
    altura1=int(input("Altura para el rectángulo 1: "))      #pedir datos
    ancho1=int(input("Ancho para el rectángulo 1: "))
    altura2=int(input("Altura para el rectángulo 2: "))
    ancho2=int(input("Ancho para el rectángulo 2: "))

    print ()
    area1=calcularArea(altura1,ancho1)                     #calcular area y perímetro del rectangulo 1
    print("El area del rectangulo 1 es: ", area1)
    perimetro1= calcularPerímetro(altura1,ancho1)
    print("El perímetro del rectangulo 1 es: ", perimetro1)
    print()                                #espacio entre resultados

    area2 = calcularArea(altura2, ancho2)                    #calcular area y perímetro del rectangulo 2
    print("El área del rectangulo 2 es: ", area2)
    perimetro2 = calcularPerímetro(altura2, ancho2)
    print("El perímetro del rectangulo 2 es: ", perimetro2)
    print(""                                        #escpacio entre resultados 
          "")

    if area1==area2:
        print("Los rectangulos tienen la misma área ")       #imprimir cual es mayor
    elif area2>area1:
        print("El rectángulo 2 tiene mayor área")
    else:
        print("El rectangulo 1 tiene mayor área ")


main()