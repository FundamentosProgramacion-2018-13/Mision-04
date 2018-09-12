#Francisco Ariel Arenas Enciso
#Cálculo de área y permitero de dos rectángulos para determinar cuál de ellos es mayor


'''Mediante el uso de operaciones arítmeticas y de los datos enviados por "main()", la función obtiene el perímetro
del primer rectángulo'''
def calcularPerimtero1(base1, altura1):
    perimetro = (base1 * 2) + (altura1 * 2)
    return perimetro


'''Mediante el uso de operaciones arítmeticas y de los datos enviados por "main()", la función obtiene el área del 
primer rectángulo'''
def calcularArea1(base1, altura1):
    area = base1 * altura1
    return area


'''Mediante el uso de operaciones arítmeticas y de los datos enviados por "main()", la función obtiene el perímetro 
del segundo rectángulo'''
def calcularPerimetro2(base2, altura2):
    perimetro2 = (base2 * 2) + (altura2 * 2)
    return perimetro2


'''Mediante el uso de operaciones arítmeticas y de los datos enviados por "main()",, la función obtiene el área del 
segundo rectángulo'''
def calcularArea2(base2, altura2):
    area2 = base2 * altura2
    return area2


'''
Mediante el uso de operadores relacionales y los datos propocionados por la función "main()", la función decide si el área 
del primer rectángulo es mayor, menor o igual a la del segundo rectángulo
'''
def decidirArea(area1, area2):
    if area1 > area2:
        return "El área del rectángulo 1 es mayor al rectángulo 2"
    if area2 > area1:
        return "El área del rectángulo 2 es mayor al rectángulo 1"
    if area1 == area2:
        return "El área es la misma"


'''
Función main, la cual controla todo el programa, envía la medida de la base y de la altura de cada rectángulo a las 
funciones correpsondientes e imprime el área y el perimetro de ambos rectángulos. De igualmanera, imprime la comparación 
del valor de las áreas.
'''
def main():
    base_rectangulo1 = int(input("Escribe la medida de la base de tu primer rectángulo: "))
    altura_rectangulo1 = int(input("Escribe la medida de la altura de tu primer rectángulo: "))
    base_rectangulo2 = int(input("Escribe la medida de la base de tu segundo rectángulo: "))
    altura_rectangulo2 = int(input("Escribe la medida de la altura de tu segundo rectángulo: "))
    perimetro1 = calcularPerimtero1(base_rectangulo1, altura_rectangulo1)
    area1 = calcularArea1(base_rectangulo1, altura_rectangulo1)
    perimetro2 = calcularPerimetro2(base_rectangulo2, altura_rectangulo2)
    area2 = calcularArea2(base_rectangulo2, altura_rectangulo2)
    mensaje = decidirArea(area1, area2)
    print("------------------------------------------------------------")
    print("El perimtero de tu primer rectágnulo es: %5.2f" % perimetro1)
    print("El área de tu primer rectágnulo es: %5.2f" % area1)
    print("------------------------------------------------------------")
    print("El perimetro de tu segundo rectágnulo es: %5.2f" % perimetro2)
    print("El área de tu segundo rectágnulo es: %5.2f" % area2)
    print("------------------------------------------------------------")
    print(mensaje)


main()