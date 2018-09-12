#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se te dan los lados de 2 rectangulos, y entonces calcula area y perimetro de ambos y ve cual es mas grande

#Calcula area del prier rectangulo
def calcularAreaA(lado1A,lado2A):
    return lado1A*lado2A

#Calcula perimetro del primer rectangulo
def calcularPerimetroA(lado1A,lado2A):
    return lado1A+lado1A+lado2A+lado2A

#Calcula area del segundo rectangulo
def calcularAreaB(lado1B,lado2B):
    return lado1B*lado2B

#Calcula area perimetro del segundo rectangulo
def calcularPerimetroB(lado1B,lado2B):
    return 2*lado1B+2*lado2B

#Compara las areas para ver cual es el mayor
def calcularMayor(lado1A,lado2A,lado1B,lado2B):
    rectanguloA = calcularAreaA(lado1A,lado2A)
    rectanguloB = calcularAreaB(lado1B,lado2B)

    if rectanguloA > rectanguloB:
        return "El mayor es el rectángulo A"
    elif rectanguloA < rectanguloB:
        return "El mayor es el rectangulo B"
    else:
        return "Son iguales"




#Llama a todas las funciones e imprkme los resulatdos de area y perimetro y te dice el resultado de la comparacion
def main():
    lado1A = float(input("Base del rectángulo A: "))
    lado2A = float(input("Altura del rectángulo A: "))
    lado1B = float(input("Base del rectángulo B: "))
    lado2B = float(input("Altura del rectángulo B: "))

    areaA = calcularAreaA(lado1A,lado2A)
    perimetroB = calcularPerimetroA(lado1A,lado2A)

    areaB = calcularAreaB(lado1B,lado2B)
    perimetroB = calcularPerimetroB(lado1B,lado2B)

    elMayor = calcularMayor(lado1A,lado2A,lado1B,lado2B)
    print("_______________________________")
    print("Rectángulo A:")
    print("Area: %.2f" % areaA , "cm2")
    print("Perímetro: %.2f" % perimetroB ,"cm" )
    print("_______________________________")
    print("Rectángulo B")
    print("Area: %.2f" % areaB ,"cm2")
    print("Perímetro: %.2f" % perimetroB ,"cm")
    print("_______________________________")
    print(elMayor)



main()