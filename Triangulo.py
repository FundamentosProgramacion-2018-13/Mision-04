#Autor Luis Mario Cervantes Ortiz
#Descripción: Determinar si es sun triángulo: Rectángulo, Isóceles o Equilátero mediante sus lados


def trianguloEquilatero(lado1,lado2,lado3): #calcular un triangulo equilatero
    if lado1<= 0 or lado2 <= 0 or lado3 <= 0 :
        return "Error"
    else:
        if lado1==lado2==lado3:
            return "Triángulo equilatero"


def trianguloIsoceles(lado1,lado2,lado3): #calcular un triangulo isóceles

    if lado1 == lado2 !=lado3  and lado1+lado2<lado3 and lado2+lado3<lado1 and lado1+lado3<lado2:
        return "Triángulo isóceles"


def trianguloRectangulo(lado1,lado2,lado3): #calcular un triangulo rectángulo

    if (lado1 *2+ lado2 **2 == lado3**2) or (lado2**2+lado3**2 == lado1**2) or (lado1**2+lado3**2 == lado1* 2):
        return "Triangulo rectangulo"


def noTriangulo (lado1,lado2,lado3): #calcular si es un triángulo

    if lado1> lado2+lado3 or lado2> lado1+lado3 or lado3>lado1+lado2:
        return "No es Triángulo"


def main(): #Preguntar y mostrar datos
    lado1=int(input("Dame un lado:"))
    lado2=int(input("Dame un segundo lado:"))
    lado3=int(input("Dame un tercer lado:"))


    totalLado=trianguloEquilatero(lado1,lado2,lado3)
    totalLado2=trianguloIsoceles(lado1,lado2,lado3)
    totalLado3=trianguloRectangulo(lado1,lado2,lado3)
    notriangulo=noTriangulo(lado1,lado2,lado3)


    if trianguloEquilatero(lado1,lado2,lado3):
        print(totalLado)
    else:
        if trianguloIsoceles(lado1,lado2,lado3):
            print(totalLado2)

        else:
            if trianguloRectangulo(lado1,lado2,lado3):
                print(totalLado3)
            else:
                print(notriangulo)




main()