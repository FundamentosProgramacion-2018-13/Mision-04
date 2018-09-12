#Nombre Diego Armando Ayala Hernández

#Matrícula A01376727

#resumen del programa: Obtiene los datos de dos rectangulos y te da el area y el perimetor de ambos

#Calcula el área de un rectángulo
def calcularArea(altura, ancho):
    area = altura * ancho
    return area

#Calcula el perímetro de un rectángulo
def calcularPerimetro(altura, ancho):
    perimetro = (2 * altura) + (2 * ancho)
    return perimetro
#Te dice cual de las dos áreas es mayor o si son iguales
def decirCualMayorArea(areaUno,areaDos):
    if areaUno > areaDos:
        return "El primer rectángulo es mayor"
    elif areaUno < areaDos:
            return "El segundo rectángulo es mayor"
    return "Los rectangulos son iguales"
#Función main: recibe las dimensiones, te da el área y perímetro de los ambos rectángulos. También te dice cual es mayor o si son iguales
def main():
    print("Escribe las dimensiones del primer rectángulo")
    alturaUno = int(input("Altura: "))
    anchoUno = int(input("Ancho: "))
    print()
    print("Escribe las dimensiones del segundo rectángulo")
    alturaDos = int(input("Altura: "))
    anchoDos = int(input("Ancho: "))
    perimetro1 = calcularPerimetro(alturaUno, anchoUno)
    perimetro2 = calcularPerimetro(alturaDos, anchoDos)
    areaUno = calcularArea(alturaUno, anchoUno)
    areaDos = calcularArea(alturaDos, anchoDos)
    mayorArea = decirCualMayorArea(areaUno, areaDos)
    print("Primer rectángulo")
    print("Área : ", (areaUno))
    print("Perímetro : ", (perimetro1))
    print("Segundo rectángulo")
    print("Área ", (areaDos))
    print("Perímetro ", (perimetro2))
    
    print(mayorArea)
