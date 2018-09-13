# Autor: Ithan Alexis Pérez Sánchez
# Determinar en base a datos de los lados, si es un triangulo y que tipo es o sino es un triangulo

# El codigo empieza después de esta linea

def calcular_Triangulos(Lado_A, Lado_B, Lado_C): # Aquí se realiza las condiciones para saber si corresponde a un tipo de trinangulo o si no es
    if Lado_A == Lado_B == Lado_C:
        return "Es Equilatero"
    else:
        if Lado_A != Lado_B == Lado_C or Lado_B != Lado_A == Lado_C or Lado_C != Lado_A == Lado_B:
            return "Es Isóseles"
        else:
            if Lado_A > Lado_B + Lado_C or Lado_B > Lado_A + Lado_C or Lado_C > Lado_A + Lado_B:
                return "No es Triangulo"
            else:
                if Lado_A != Lado_B != Lado_C:
                    return "Es Escaleno"



def main():
    Lado_A = int(input("Ingresa el valor del lado A: "))
    Lado_B = int(input("Ingresa el valor del lado B: "))
    Lado_C = int(input("Ingresa el valor del lado C: "))
    Aviso = calcular_Triangulos(Lado_A, Lado_B, Lado_C)
    print(Aviso)

main()