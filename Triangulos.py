#Autor: Jesús Zabdiel Sanchez Chavez
#Descripcion: Lee el valor de los tres lados de un triangulo y dice si existe o no y qué tipo de triángulo es.

def identificarTrangulo (a, b,c):

    if c**2 == a**2 + b**2 or a**2 == b**2 + c**2  or b**2 == c**2+a**2:
        return "Es un triángulo rectángulo"
    elif a==b or b==c or c ==a:
        return "Es un triangulo isóscceles"
    elif a == b == c:
        return "Es un trinagulo equilatero"
    else:
        return "Estos lados no corresponden a ningun triangulo"

def main():
    ladoA = int(input("Teclea el valor del primer lado: "))
    ladoB = int(input("Teclea el valor del segundo lado: " ))
    ladoC = int(input("Teclea el valor del tercer lado: "))
    print (identificarTrangulo(ladoA,ladoB,ladoC))


main()