#Autor: Diana Marisol Medina Bravo
#Lee el valor de cada uno de los lados de un triángulo y determina si es rectangulo, isosceles o equilatero
#Al probar el programa necesita de todos los decimales del valor de algun lado si es la hipotenusa debido a que si
#no tiene todos estos decimales la marcara al triangulo como isosceles. Un numero de prueba con decimales es 8.48528137423857 , 6 y 6


#Función para determinar el tipo de triangulo
#Recibe los lados y regresa el tipo del triangulo
def determinarTipoTriangulo(lado1, lado2, lado3):
    hipotenusa3= ((lado1 ** 2) + (lado2 ** 2)) ** 0.5
    hipotenusa1 = ((lado2 ** 2) + (lado3 ** 2)) ** 0.5
    hipotenusa2 = ((lado1 ** 2) + (lado3 ** 2)) ** 0.5

    if lado1==lado2 and lado3==lado2:
        tipoTriangulo= "Equilatero"
        return tipoTriangulo

    elif lado1==lado2 and lado2!=lado3:
        if lado3== hipotenusa3:
            tipoTriangulo="Rectángulo"
            return tipoTriangulo
        else:
            return "Isósceles"

    elif lado1 == lado3 and lado2!=lado3:
        if lado2 == hipotenusa2:
            return "Rectángulo"
        else:
            return "Isósceles"

    elif lado2 == lado3 and lado2 != lado1:
        if lado1 == hipotenusa1:
            return "Rectángulo"
        else:
            return "Isósceles"

    elif lado3 == hipotenusa3:
        return "Rectángulo"

    elif lado1 == hipotenusa1:
        return "Rectángulo"

    elif lado2 ==hipotenusa2:
        return "Rectángulo"

    else:
        return "Estos lados no corresponden a un triángulo"


#Función principal
def main():
    lado1=float(input("Teclee el primer lado del triángulo: "))
    lado2=float(input("Teclee el segundo lado del triángulo: "))
    lado3=float(input("Teclee el tercer lado del triángulo: "))
    if lado1>0 and lado2>0 and lado3>0:
        tipoTriangulo=determinarTipoTriangulo(lado1, lado2, lado3)
        print (tipoTriangulo)
    else:
        print ("Estos lados no corresponden a un triángulo")




main()