# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el perímetro y área de dos rectángulos e indica el area mayor


#Calcula el área de un rectángulo dado su base y altura
def calcularAreas(b, h):
    return b*h


#Calcula el perímetro de un rectángulo dado su base y altura
def calcularPerimetro(b,h):
    return (2*b)+(2*h)


#Calcula el área de los dos rectángulos y regresa el mayor
def esMayorAreaUno(A1, A2):
    if A1 == A2:
        return "Las áreas de ambos rectángulos son iguales"
    if A2 > A1:
        return "El segundo rectángulo tiene el área mayor"
    return "El primer rectángulo tiene el área mayor"


#Preguntar datos al usuario e imprimir los resultados
def main():
    baseUno = int(input("Base del primer rectángulo: "))
    alturaUno = int(input("Altura del primer rectángulo: "))
    baseDos = int(input("Base del segundo rectángulo: "))
    alturaDos = int(input("Altura del primer rectángulo: "))

    areaUno = calcularAreas(baseUno, alturaUno)
    areaDos = calcularAreas(baseDos, alturaDos)
    print()
    print("Area del primer rectángulo: %d" % areaUno)
    print("Perímetro del primer rectángulo: %d" % calcularPerimetro(baseUno, alturaUno))
    print("Area del segundo rectángulo: %d" % areaDos)
    print("Perímetro del segundo rectángulo: %d" % calcularPerimetro(baseDos, alturaDos))
    print("%s" % (esMayorAreaUno(areaUno, areaDos)))


#Ejecutar main()
main()
