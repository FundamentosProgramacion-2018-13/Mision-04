# Autor: Jonathan Sanabria Rocha
# Descripcion: Saber que tipo de triangulo es, con respecto a la longitud de sus lados y si existe.


# Indica que tipo de triangulo es
def IndicarTipoTriangulo(lado1,lado2,lado3):
    if lado1 == lado2 and lado2 == lado3:
       equilatero = "Es un triangulo equilatero"
       return equilatero
    elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado3 != lado2) or (lado3 == lado2 and lado2 != lado1):
        isosceles = "Es un triangulo  isosceles"
        return isosceles
    elif lado1**2 + lado2**2 == lado3**2 or lado2**2+lado3**2 == lado1**2 or lado1**2 + lado3**2 == lado2**2:
        rectangulo = "Es un triangulo rectangulo"
        return rectangulo
    else:
        trianguloInexistente = "Estos lados no corresponden a un triangulo"
        return trianguloInexistente


# Funcion principal
def main():
    lado1 = int(input("Teclea el valor del lado 1: "))
    lado2 = int(input("Teclea el valor del lado 2: "))
    lado3 = int(input("Teclea el valor del lado 3: "))
    print(IndicarTipoTriangulo(lado1,lado2,lado3))


# Llama a la funcion principal
main()


