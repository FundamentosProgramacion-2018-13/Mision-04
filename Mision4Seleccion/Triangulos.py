# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lea el valor de cada uno de los lados de un triángulo (puede ser en cualquier orden).

# Se determina el triángulo en base a sus características.
def determinarTriangulo(A, B, C):
    if A == B != C or A != B == C or A == C != B:
        tipoDeTriangulo = "Isósceles"
        return tipoDeTriangulo

    elif A == B == C:
        tipoDeTriangulo = "Equilátero"
        return tipoDeTriangulo

    elif A != B != C & C != A:
        tipoDeTriangulo = "Rectángulo"
        return tipoDeTriangulo



def main():
    # Se obtiene la longitud de los lados de un triángulo.
    ladoA = int(input("Introduce el primer lado del triángulo: "))
    ladoB = int(input("Introduce el segundo lado del triángulo: "))
    ladoC = int(input("Introduce el tercer lado del triángulo: "))

    # Filtra la información dada por el usuario.
    if (ladoA > 0) & (ladoB > 0) & (ladoC > 0):
        tipoDeTriangulo = determinarTriangulo(ladoA, ladoB, ladoC)
        print("El triángulo es de tipo %s " % tipoDeTriangulo)

    else:
        print("Estos lados no corresponden a un triángulo.")
    
main()