"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998
Descripción: Dados los lados de un triángulo, se define su tipo (equilatero, isóceles, rectángulo o si no pertenece a ninguno de los tres tipos)

"""

#Define si el triánuglo es equilatero, isóceles, rectángulo o si no pertenece a ninguno de los tres tipos. Esto lo hace con base en las medidas de sus lados
def definirTriangulo(lado1, lado2, lado3):

    #Define si el triángulo es equilatero
    if lado1 == (lado2 and lado1 == lado3) and ((lado1 and lado2 and lado3) > 0):
        return "Es Equilatero"

    #Define si el triángulo es rectángulo
    if (lado1 == (((lado3**2)+(lado2**2))**.5)) or (lado2 == ((lado1**2)+(lado3**2))**.5) or (lado3 == ((lado1**2)+(lado2**2))**.5) and ((lado1 and lado2 and lado3) > 0):
        return "Es Rectángulo"

    #Define si el triángulo es isóceles
    if ((lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1)) and ((lado1 and lado2 and lado3) > 0):
        return "Es Isóceles"
    else:
        return "Estos lados no corresponden a un triángulo"


#Imprime el tipo de triángulo que es
def imprimir(lado1, lado2, lado3):
    print(definirTriangulo(lado1, lado2, lado3))


#Agrupa las demás funciones para resolver el problema
def main():
    lado1 = float(input("Primer Lado: "))
    lado2 = float(input("Segundo Lado: "))
    lado3 = float(input("Tercer Lado: "))
    if (lado1 <= 0) or (lado2 <= 0) or (lado3 <= 0):
        return print("El triángulo no existe")
    tipoDeTriangulo = imprimir(lado1, lado2, lado3)


#Llama a la función principal para resolver el problema
main()
