#Autor Zabdiel Valentin.
#En base a los lados de un triangulo, determinar si es Rectangulo, Isósceles o Equilátero, si no corresponde a alguno marca error.


def calculoTriangulo(a, b, c):
    x=a**2
    y=b**2
    z=c**2
    if a<=0 or b<=0 or c<=0:
        return "Estos lados no corresponden a un triángulo"
    if int(float(x+y))==int(float(z))or int(float(x+z))==int(float(y))or int(float(z+y))==int(float(x)):
        return "es triangulo cuadrado"

    if int(float(a))==int(float(b)) and int(float(a))==int(float(c)):
        return "es triangulo Equilatero"

    if int(float(a))==int(float(b)) or int(float(a))==int(float(c))or int(float(b))==int(float(c)):
        return "es triangulo Isósceles"
    else:
        return "Estos lados no corresponden a un triángulo"


def main():
    a = float(input("Lado A: "))
    b = float(input("Lado b: "))
    c = float(input("Lado C: "))
    triangulo = calculoTriangulo(a,b,c)
    print(triangulo)
main()
