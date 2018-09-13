#Autor: David Alejandro Nicolás Palos
#Describir el tipo de triangulo de acuerdo a sus 3 lados dados


def definirTriangulo(ladoUno,ladoDos, ladoTres): #Compara todos los lados del triangulo para determinar el tipo
    if ladoUno == ladoDos and ladoDos==ladoTres:
        return "Triangulo Equilatero"
    else:
        if ladoUno == (((ladoDos)**2)+((ladoTres)**2))**.5:
            return "Triangulo Rectangulo"
        else:
            if ladoDos == (((ladoUno)**2)+((ladoTres)**2))**.5:
                return "Triangulo Rectangulo"
            else:
                if ladoTres == (((ladoDos)**2)+((ladoUno)**2))**.5:
                    return "Triangulo Rectangulo"
                else:
                    if ladoUno == ladoDos or ladoDos == ladoTres or ladoTres == ladoUno:
                        return "Triangulo Isoceles"
                    else:
                        return "Estos lados no corresponden a un triángulo"


def main(): #funcion main, lee e imprime resultados
    ladoUno = float(input("Longitud del primer lado: "))
    ladoDos = float(input("Longitud del segundo lado: "))
    ladoTres = float(input("Longitud del tercer lado: "))
    print("")
    print(definirTriangulo(ladoUno,ladoDos,ladoTres))

main()