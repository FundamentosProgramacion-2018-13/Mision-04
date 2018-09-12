#Rodolfo Anibal Altamirano Sánchez, A0377949
#Te dan los lados de una triángulo, y tienes que averiguar si es rectángulo, isóceles o equilátero y si no es ninguno de estos imprime error

# Una vez que te dan los tres lados, se calcula que tipo de trióngulo es con teorema de pitágoras y con compaacion de lados
def calcularTipo(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return "Error"
    elif a==b and a==c:
        return "Es un triángulo equilátero"
    #Un triángulo isóceles tiene dos de sus lados iguales, pero el lado diferente nunca puede ser mayor o igual a la suma de los dos lados igales, si asi ocurre deja de ser un triángulo y se convierte en una linea
    elif (a==b and (a > c or a < c)and a+b > c) or (a==c and (a > b or a < b) and a+c > b) or (b==c and(b > a or b < a)and b+c > a):
        return "Es un triángulo isóceles"
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        return "Es un triángulo rectángulo"
    else:
        return "Este triángulo no existe"

# se llama la funcion e imprime los resultados
def main():
    #Se establecen los valores de los lados
    a = int(input("Lado 1: "))
    b = int(input("Lado 2: "))
    c = int(input("Lado 3: "))

    tipoDeTriangulo = calcularTipo(a,b,c)

    print(tipoDeTriangulo)
main()