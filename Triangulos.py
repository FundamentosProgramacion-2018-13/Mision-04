#Irma Gómez Carmona, A01747743
#Determinar segun las medidas si se trata de un triangulo, y si lo es, definir que tipo de triangulo es

def determinarSiEsTriangulo(lado1, lado2, lado3): #Es un tringulo si la suma de dos de sus lados es mayor a la del tercero
    if lado1+lado2>lado3 and lado1+lado3>lado2:
        return True
    return False


def determinarQueTrianguloEs (lado1,lado2,lado3):#Compara sus lados para determinar que tipo de triangulo es
        if lado1==lado2 and lado1==lado3:
            tipo="Equilatero"
        elif  lado1==lado2 or lado1==lado2 or lado2==lado3:
            tipo="Isosceles"
        elif  (lado1**2+lado2**2)**0.5==lado3 or (lado2**2+lado3**2)**0.5==lado1 or (lado1**2+lado3**2)**0.5==lado2:
            tipo="Rectangulo"
        else:
            tipo="Escaleno"

        return tipo


def main (): #Obtener valores, llamar a las otras funciones y mostrar resultados
    lado1 = int(input("Medida del lado 1:"))
    lado2 = int(input("Medida del lado 2:"))
    lado3 = int(input("Medida del lado 3:"))

    valido= determinarSiEsTriangulo(lado1,lado2,lado3)

    if valido==True:
        tipo= determinarQueTrianguloEs(lado1,lado2,lado3)
        print("Tipo de triánngulo: ", tipo)
    else:
        print("Estos lados no corresponden a un triangulo")

main ()