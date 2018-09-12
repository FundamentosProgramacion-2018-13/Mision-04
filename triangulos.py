#Mariana Caballero Cabrera  A01376544
# Recibe los lados de un triángulo y calcula que tipo de triángulo es


# Determina el tipo de triángulo según sus lados
def determinarTriangulo (lado1,lado2,lado3):

    if lado1 == lado2 and lado2 == lado3:
        triangulo = "isosceles"

    elif lado1 == lado2 != lado3 :
        triangulo = "equilatero"

    elif lado1 != lado2 != lado3:
        triangulo = "rectángulo"

    else:
        triangulo = "No existe"

    return triangulo



#Función principal
def main():

    lado1 = int(input("Teclea el lado 1 del triángulo: "))
    lado2 = int(input("Teclea el lado 2 del triángulo: "))
    lado3 = int(input("Teclea el lado 3 del triángulo: "))

    if lado1 >0 and lado2 >0 and lado3 >0:
        tipoTriangulo = determinarTriangulo(lado2,lado1,lado3)
        print ("Los tres lados del triángulo son: ", lado1,"cm ,", lado2,"cm ,", lado3,"cm")
        print ("Por lo tanto es un triángulo",tipoTriangulo)

    else:
        print("Estos lados no corresponden a un triángulo")


#Llamamos a la función principal
main ()