# Autor: Ithan Alexis Pérez Sánchez
# Calcular el área y perímetro de dos rectángulos, y determinar quien es mas grande, en base a su área

# El codigo empieza después de esta linea

def Calcular_Area(Valor_1A, Valor_1B):
    Area_Nm1 = Valor_1A * Valor_1B
    return Area_Nm1
            # Las 3 funciones cumplen el calculo de sacar area, perimetro e imprimir los valores del primer rectangulo
def Calcular_Perimetro(Valor_1A, Valor_1B):
    Perimetro_Nm1 = 2*Valor_1A + 2*Valor_1B
    return Perimetro_Nm1

def Imprimir(Valor_1A, Valor_1B):
    print("El área es: %.2f" % (Calcular_Area(Valor_1A, Valor_1B)))
    print("El perímetro es: %.2f" % (Calcular_Perimetro(Valor_1A, Valor_1B)))
# --------------------------------------------------------------------------------------******

def Calcular_Area_2(Valor_2A, Valor_2B):
    Area_Nm2 = Valor_2A * Valor_2B
    return Area_Nm2
            # Las 3 funciones cumplen el calculo de sacar area, perimetro e imprimir los valores del segundo rectangulo
def Calcular_Perimetro_2(Valor_2A, Valor_2B):
    Perimetro_Nm2 = 2*Valor_2A + 2*Valor_2B
    return Perimetro_Nm2

def Imprimir2(Valor_2A, Valor_2B):
    print("El área es: %.2f" % (Calcular_Area_2(Valor_2A, Valor_2B)))
    print("El perímetro es: %.2f" % (Calcular_Perimetro_2(Valor_2A, Valor_2B)))

# --------------------------------------------------------------------------------------******

def Comparar(Valor_1A, Valor_1B, Valor_2A, Valor_2B):
    if Calcular_Area(Valor_1A, Valor_1B) > Calcular_Area_2(Valor_2A, Valor_2B):
        return "Es mayor el Primer Rectangulo"
    else:
        if Calcular_Area(Valor_1A, Valor_1B) < Calcular_Area_2(Valor_2A, Valor_2B):
            return "Es mayor el Segundo Rectangulo"
    return "Son iguales"

# Aquí hace la comparación de cual es más grande, pequeño o si son iguales los rectangulos

def main(): # Aquí se ingresan los valores e imprime la comparación
    Valor_1A = int(input("Ingresa el valor del lado A: "))
    Valor_1B = int(input("Ingresa el valor del lado B: "))

    Imprimir (Valor_1A, Valor_1B)

    Valor_2A = int(input("Ingresa el valor del lado A: "))
    Valor_2B = int(input("Ingresa el valor del lado B: "))

    Imprimir2 (Valor_2A, Valor_2B)
    Aviso = Comparar(Valor_1A, Valor_1B, Valor_2A, Valor_2B)
    print(Aviso)


main()
