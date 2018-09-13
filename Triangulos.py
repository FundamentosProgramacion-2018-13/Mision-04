#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripción: Determina tipo de traingulo y si existe

#Indica mediante selección que tipo de triangulo es y regresa cadena
def indicarTipo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Es un triangulo equilatero"

    elif lado1 == lado2 and lado3 != lado2:
         return "Es un triangulo isosceles"

    elif lado2 ==  lado3 and lado3 != lado1:
        return "Es un triangulo isosceles"

    elif lado3 == lado1 and lado1 != lado2:
        return "Es un triangulo isosceles"

    elif ((lado1**2)+(lado2**2)==(lado3**2)) or ((lado1**2)+(lado3**2)==(lado2**2)) or ((lado2**2)+(lado3**2)==(lado1**2)):
        return "Es un triangulo rectangulo"

    else:
        return "No existe el triangulo"

#función principal
def main():
    lado1 = int(input("Ingresa la longitud del primer lado: "))
    lado2 = int(input("Ingresa la longitud del segundo lado: "))
    lado3 = int(input("Ingresa la longitud del tercer lado: "))
    print ("")
    total = indicarTipo(lado1, lado2, lado3)
    print (total)


main()
