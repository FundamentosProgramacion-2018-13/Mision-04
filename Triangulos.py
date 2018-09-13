#Autor: Alan Diaz Carrera
#Descripcion: Obtener si existe el triangulo y el tipo de triangulo dependiendo de sus lados

def existir(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        existe = 1
        return existe
    if lado2 == lado3 or lado2 == lado1 or lado1 == lado3:
        existe = 2
        return existe
    if lado3 == ((lado2**2)+(lado1**2))**0.5:
        existe = 3
        return existe
    if lado2 == ((lado3**2)+(lado1**2))**0.5:
        existe = 3
        return existe
    if lado1 == ((lado2**2)+(lado3**2))**0.5:
        existe = 3
        return existe
    existe = 4
    return existe
def main():
    lado1 = int(input("Longitud del lado 1 del triangulo: "))
    lado2 = int(input("Longitud del lado 2 del triangulo: "))
    lado3 = int(input("Longitud del lado 3 del triangulo: "))
    existe = existir(lado1, lado2, lado3)
    if existe == 1:
        print("Este es un triangulo equilatero")
    if existe == 2:
        print("Este es un triangulo isosceles")
    if existe == 3:
        print("Este es un triangulo rectangulo")
    if existe == 4:
        print("Estos lados no corresponden a un triangulo")

main()