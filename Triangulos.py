#Francisco Ariel Arenas Enciso
#Determinación de un triángulo de acuerdo a la medida de sus lados


'''
Mediante el uso de operadores lógicos y relacionales, y de los datos enviados por "main()",
la función decide que tipo de triángulo es.
'''
def decidirTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
       return "forman un triángulo equilatero"
    elif lado1 == lado2 or lado1 == lado3:
        return "forman un triángulo isósceles"
    elif lado2 == lado3:
        return "forman un triángulo isósceles"
    elif ((lado1**2)+(lado2**2))**0.5 == lado3:
        return "forman un triángulo rectángulo"
    elif ((lado2 ** 2) + (lado3** 2)) ** 0.5 == lado1:
        return "forman un triángulo rectángulo"
    elif ((lado1 ** 2) + (lado3 ** 2)) ** 0.5 == lado2:
        return "forman un triángulo rectángulo"
    else:
       return "no pertenecen a ningún triángulo"


'''
Función main, la cual controla todo el programa, envía las medidas de los lados a la función "decidirTriangulo"
e imprime el mensaje de acuerdo al resultado obtenido de la función.
'''
def main():
    lado1 = int(input("Escribe la medida del primer lado de tu figura: "))
    lado2 = int(input("Escribe la medida del segundo lado de tu figura: "))
    lado3 = int(input("Escribe la medida del tercer lado de tu figura: "))
    mensaje = decidirTriangulo(lado1, lado2, lado3)
    print("---------------------------------")
    print("Las medidas dadas %s" % (mensaje))


main()