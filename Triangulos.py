# Oscar Alejandro Torres Maya, A01377686
# Leer los lados de los triángulos y decir que tipo de triángulo es

# Condición para que sea triángulo rectángulo
def trianguloRectangulo(lado1,lado2,lado3):
    if lado1 > lado2 and lado1 > lado3:
        hyp = ((lado3**2)+(lado2**2))**0.5
        return hyp
    elif lado2 > lado1 and lado2 > lado3:
        hyp = ((lado1 ** 2) + (lado3 ** 2)) ** 0.5
        return hyp
    elif lado3 > lado1 and lado3 > lado2:
        hyp = ((lado1 ** 2) + (lado2 ** 2)) ** 0.5
        return hyp


# Función principal
def main():
    lado1 = float(input("Cuál es el primer lado del triángulo? "))
    lado2 = float(input("Cuál es el segundo lado del triángulo? "))
    lado3 = float(input("Cuál es el tercer lado del triángulo? "))
    triangulo = trianguloRectangulo(lado1,lado2,lado3)

    if lado1 <= 0 and lado2 <= 0 and lado3 <= 0:
        print("Estos lados no corresponden a un triángulo")

    elif lado1 == lado2 and lado2 == lado3 and lado3 == lado1:
        print("El triángulo es equilatero")

    elif lado2 == lado3 or lado1 == lado2 or lado3 == lado1:
        print("El triángulo es isóceles")

    elif triangulo == lado1 or triangulo == lado2 or triangulo == lado3:
        print("El triángulo es un triángulo rectángulo")
    else:
        print("Este triángulo no es equilatero, ni isóceles y ni triángulo rectángulo")

# Llamada de función principal
main()