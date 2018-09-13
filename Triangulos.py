# Autor: Carlos Alberto Reyes Ortiz
# Te dice que tipo de triángulo es de acuerdo sus longitudes (Rectángulo, Isósceles, Equilátero)



def definirQueTipoDeTrianguloEs(ladoUno,ladoDos, ladoTres):# Te dice si un triángulo es equilátero, isóceles
    #                                                        o rectángulo de acuerdo a sus longitudes
    if ladoDos == ladoUno and ladoUno ==ladoTres:
        return "De acuerdo a sus longitudes es un triángulo equilátero"
    elif ladoUno == ladoDos or ladoDos == ladoTres or ladoUno == ladoTres:
        return "De acuerdo a sus longitudes es un triángulo isóceles"
    elif ladoUno**2 == ladoDos**2 + ladoTres**2 or ladoDos**2 == ladoUno**2 + ladoTres**2 or ladoTres**2 == ladoUno**2 + ladoDos**2:
        return "De acuerdo a sus longitudes es un triángulo Rectángulo"
    else: return "Estos lados no corresponden a un triángulo"




def main(): # Función principal: Dada sus lados en el orden que sea, te dice si es rectángulo, equilátero o isóceles
    print("Dame los lados del triángulo en el orden que quieras")
    ladoUno = float(input("Lado uno: "))
    ladoDos = float(input("Lado dos: "))
    ladoTres = float(input("Lado tres: "))
    print()
    tipoDeTriangulo = definirQueTipoDeTrianguloEs(ladoUno, ladoDos, ladoTres)
    print(tipoDeTriangulo)


#llamar función
main()