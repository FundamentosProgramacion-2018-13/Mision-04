#Emiliano Heredia A01377072
#Dado la base y area de dos rectangulos, calcula el area y perimetro de ambos y deterima el de mayor area.

def main():
    base1 = int(input("Ingrese la base del rectangulo 1: "))
    altura1 = int(input("Ingrese la altura  del rectangulo 1: "))
    base2 = int(input("Ingrese la base del rectangulo 2: "))
    altura2 = int(input("Ingrese la altura del rectangulo 2: "))

    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)

    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)

    print("Rectangulo #1, area: %.2f perimetro: %.2f" %(area1,perimetro1))
    print("Rectangulo #2, area: %.2f perimetro: %.2f" %(area2, perimetro2))

    if(area1>area2):
        print("El rectangulo #1 tiene mayor area que el rectangulo #2")
    elif(area1<area2):
        print("El rectangulo #2 tiene mayor area que el rectangulo #1")
    else:
        print("Ambos rectangulos tiene la misma area. ")

#calcula el area de un rectangulo dado la base y altura
def calcularArea(base, altura):
    return base*altura

#calcula el perimetro de un rectangulo dado la base y altura
def calcularPerimetro(base, altura):
    return 2*base + 2*altura


main()