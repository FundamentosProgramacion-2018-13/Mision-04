#Autor: David Alejandro Nicolás Palos
#Recibir el número de paquetes comprados, calcular el decuento y el total de la compra



def calcularDescuento(paquetesComprados): #analiza el número de paquetes comprados y le adjunta un String dependiendo del descuento
    if paquetesComprados > 0:
        if paquetesComprados < 10:
            descuento = ""
            return descuento
        else:
            if paquetesComprados < 20:
                descuento = "Descuento del 20%"
                return descuento
            else:
                if paquetesComprados < 50:
                    descuento = "Descuento del 30%"
                    return descuento
                else:
                    if paquetesComprados < 100:
                        descuento = "Descuento del 40%"
                        return descuento
                    else:
                        descuento = "Descuento del 50%"
                        return descuento
    else:
        print("Error: Número de paquetes inválido")


def calcularTotal(paquetesComprados, descuento): #Compara el número de paquetes comprados contra sus String de descuento y determina si se debe aplicar o no

    if paquetesComprados > 0:
        if descuento == "":
            total = paquetesComprados * 150
            return total
        else:
            if descuento == "Descuento del 20%":
                total = (paquetesComprados * 1500) - ((paquetesComprados*1500)*.2)
                return total
            else:
                if descuento == "Descuento del 30%":
                    total = (paquetesComprados * 1500) - ((paquetesComprados * 1500) * .3)
                    return total
                else:
                    if descuento == "Descuento del 40%":
                        total = (paquetesComprados * 1500) - ((paquetesComprados * 1500) * .4)
                        return total
                    else:
                        if descuento == "Descuento del 50%":
                            total = (paquetesComprados * 1500) - ((paquetesComprados * 1500) * .5)
                            return total
    else:
        return 0

def main(): #funcion main, lee e imprime resultados
    paquetesComprados = int(input("Número de paquetes comprados: "))
    descuento = calcularDescuento(paquetesComprados)

    print("")
    print(calcularDescuento(paquetesComprados))
    print("")
    print("Total: ", calcularTotal(paquetesComprados, descuento))

main()