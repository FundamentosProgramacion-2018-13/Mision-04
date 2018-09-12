# Luis Jonathan Rosas Ramos
# A01377942
# Determinar si un triangulo es Rectangulo, Isoceles o Equilatero,con base en sus lados

# Funcion para calcular que tipo de triangulos es
def calcularTriangulo(a,b,c):
    # se iguala el lado uno al dos y el dos al tres, ya que si estas condiciones se cumplen
    # quiere decir que el riangulo tiene dos lados igaules entonces es quilatero
    if a==b and b==c:
        return "El triagulo es Equilatero"
    # se comparan los tres ya que si son iguales entonces es isoceles
    elif a==b or b == c or c == a:
        return "El triangulo es Isoceles"
    # En este caso se pone != ya que si ninguno es igual entonces el traingulo sera escaleno
    elif a != b or b != c or c != a:
        return "El triangulo es escaleno"
    else:
        return "Estos lados no corresponden a un triangulo"


# Funcion principal
def main():
    a = int(input("¿Cual es tu lado uno?: "))
    b = int(input("¿Cual es tu lado dos?: "))
    c = int(input("¿Cual es el lado tres: "))
    triangulo = calcularTriangulo(a,b,c)
    print(triangulo)

# Llamar la funcion
main()