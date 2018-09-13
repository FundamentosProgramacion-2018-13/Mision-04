#Autor Luis Mario Cervantes Ortiz
#Descripción: Recibir dimensiones de 2 rectangulos, sacar su area y perímetro y decir cual tiene el área más grande


def rectangulo1Area(base1,altura1): #calcular el area del rectangulo1

    area1=base1*altura1
    return area1

def rectangulo2Area(base2,altura2):#calcular el area del rectangulo2

    rectangulo2Area=base2*altura2
    return rectangulo2Area


def compararArea(totalArea1,totalArea2): #Comparar las áreas

    if totalArea1>totalArea2:
        return totalArea1
    else:
        if totalArea2>totalArea1:
            return totalArea2
        else:
            if totalArea1==totalArea2:
                print("Ninguno, los 2 tienen misma area")


def rectangulo1Perimetro1(base1,altura1): #calcular el perímetro del rectangulo1

    perimetro1 =2*(base1+altura1)
    return perimetro1


def rectanguloPerimetro2(base2,altura2):#calcular el perímetro del rectangulo2

    perimetro2=2*(base2+altura2)
    return perimetro2


def main():#Preguntar datos e imprimir

    base1=int(input("Dime la base del primer rectangulo:"))
    altura1=int(input("Dime la altura del primer rectangulo:"))
    base2=int(input("Dime la base del segundo rectangulo:"))
    altura2=int(input("Dime la altura del segundo rectangulo:"))

    totalArea1=rectangulo1Area(base1,altura1)
    totalArea2=rectangulo2Area(base2,altura2)
    totalPerimetro1=rectangulo1Perimetro1(base1,altura2)
    totalPerimetro2=rectanguloPerimetro2(base2,altura2)



    print("El total de perimetro del primer rectangulo es: %.2f"%(totalPerimetro1))
    print("El total de perimetro del segundo rectangulo es: %.2f"%(totalPerimetro2))

    print("El total del primer rectángulo es: %.2f"% (totalArea1))
    print("El total del segundo rectángulo es: %.2f"% (totalArea2))

    print("El rectangulo con mayor área es el:", compararArea(totalArea1,totalArea2))


main()