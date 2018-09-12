#Mariana Caballero Cabrera  A01376544

# Calcular área y perímetro de 2 rectangulos, determinar cuál tiene mayor área


# Calcular área del rectángulo 1

def calcularArea1 (base1,altura1):
    area1 = base1*altura1
    return area1

#calcular el área del rectángulo 2

def calcularArea2 (base2,altura2):
    area2 = base2*altura2
    return area2

#Calcular el perímetro del rectángulo 1

def calcularPerimetro1 ( base1,altura1):
    perimetro1 = (base1*2)+(altura1*2)
    return perimetro1

#Calcular el perímtro del rectángulo 2

def calcularPerimetro2 (base2, altura2):
    perimetro2 = (base2 * 2) + (altura2 * 2)
    return perimetro2



# función principal

def main():

    base1 = int(input("Teclea el tamaño de la base del primer rectángulo: "))
    altura1 = int(input("Teclea el tamaño de la altura del primer rectángulo: "))
    base2 = int(input("Teclea el tamaño de la base del segundo rectángulo: "))
    altura2 = int(input("Teclea el tamaño de la altura del segundo ractángulo: "))

    area1 = calcularArea1 (base1,altura1)
    area2 = calcularArea2 (base2,altura2)

    print ("---------------------------------------------------")

    if area1 < area2:
        print("El ractángulo 2 es mayor con: ", area2, "cm2")
        print("El ractángulo 1 es menor con: ", area1, "cm2")
    else:
        print("El ractángulo 1 es mayor con: ", area1, "cm2")
        print("El ractángulo 2 es menor con: ", area2, "cm2")

    perimetro1 = calcularPerimetro1 (base1, altura1)
    perimetro2 = calcularPerimetro2 (base2,altura2)

    print ("------------------------------------------------------------------")
    print ("El perímetro del rectángulo 1 es: ", perimetro1, "cm")
    print("El perímetro del rectángulo 2 es: ", perimetro2, "cm")



#llamamos a la función principal

main()