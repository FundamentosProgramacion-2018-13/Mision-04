#Jesús Roberto Herrera Vieyra // A01377230
#Programa para clasificar triángulos

#Evalua si es equilátero
def esEquilatero(ladoA, ladoB, ladoC):
    if ladoA==ladoB and ladoB==ladoC:
        return "equilátero"
    else:
        return "not"


#Evalua si es isoceles (Tomando en cuanta que la definicion de
#triangulo isóceles es "Que tiene dos lados iguales, este se desplegará aunque el triángulo igual sea equilátero
def esIsoceles(ladoA,ladoB,ladoC):
    if ladoA==ladoB or ladoA == ladoC or ladoB==ladoC:
        return "isóceles"
    else:
        return "not"


#Evalua si es un triángulo rectángulo meidante pitágoras
def esRectangulo(ladoA, ladoB, ladoC):
    if ladoA**2 == (ladoB**2 + ladoC**2) or ladoB**2 == (ladoA**2+ladoC**2) or ladoC**2 == (ladoA**2+ladoB**2):
        return "rectángulo"
    else:
        return "not"


#Funcion principal
def main():
    ladoA = float(input("teclee el primer lado: "))
    ladoB = int(input("teclee el segundo lado: "))
    ladoC = int(input("teclee el tercer lado: "))

    isoceles = esIsoceles(ladoA,ladoB,ladoC)
    equilatero = esEquilatero(ladoA,ladoB,ladoC)
    rectangulo = esRectangulo(ladoA,ladoB,ladoC)

    if ladoA + ladoB > ladoC and ladoB + ladoC > ladoA and ladoA + ladoC > ladoB:
        if equilatero == "equilátero":
            print("Es equilátero")
        if rectangulo == "rectángulo":
            print("Es rectángulo")
        if isoceles == "isóceles":
            print("Es isoceles")
        if equilatero == "not" and rectangulo == "not" and isoceles == "not":
            print("Estos lados no corresponden a un triángulo de estos tipos")
    else:
        print("Los lados no corresponden a un triangulo")


main()