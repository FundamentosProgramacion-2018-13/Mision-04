# Carlos Badillo García
# Programa que lee el número de paquetes comprados y despliega la cantidad descontada y el total a pagar


def calcularDescuento(cantidadPaquetes): #Calcular el descuento que se hace dependiendo la cantidad de paquetes
    if cantidadPaquetes <= 0:
        return 0

    elif cantidadPaquetes >= 1 and cantidadPaquetes <= 9:
        return 0

    elif cantidadPaquetes >= 10 and cantidadPaquetes <= 19:
        return (cantidadPaquetes * .20) * 1500

    elif cantidadPaquetes >= 20 and cantidadPaquetes <= 49:
        return "El descuento es de: ", (cantidadPaquetes * .30) * 1500

    elif cantidadPaquetes >= 50 and cantidadPaquetes <= 99:
        return "El descuento es de: ", (cantidadPaquetes * .40) * 1500

    elif cantidadPaquetes >= 100:
        return "El descuento es de: ", (cantidadPaquetes * .50) * 1500


def indicarTotalaPagar(cantidadPaquetes): #Indicar la cantidad total a pagar
    if cantidadPaquetes <= 0:
        return "Error"

    elif cantidadPaquetes >= 1 and cantidadPaquetes <= 9:
        return (cantidadPaquetes * 1500)

    elif cantidadPaquetes >= 10 and cantidadPaquetes <= 19:
        return (cantidadPaquetes * 1500) - ((cantidadPaquetes * .20) * 1500)

    elif cantidadPaquetes >= 20 and cantidadPaquetes <= 49:
        return (cantidadPaquetes * 1500) - ((cantidadPaquetes * .30) * 1500)

    elif cantidadPaquetes >= 50 and cantidadPaquetes <= 99:
        return (cantidadPaquetes * 1500) - ((cantidadPaquetes * .40) * 1500)

    elif cantidadPaquetes >= 100:
        return (cantidadPaquetes * 1500) - ((cantidadPaquetes * .50) * 1500)


def main(): #El usuarion itrude la cantidad de paquetes, el programa imprime la cantidad descontada y la cantidad total a pagar
    cantidadPaquetes = int(input("La cantidad de paquetes es de: "))
    descuento = calcularDescuento(cantidadPaquetes)
    totalPagar = indicarTotalaPagar(cantidadPaquetes)
    print("La cantidad descontada es de: $ %.2f" % descuento)
    print("El total a pagar es de: $ %.2f" % totalPagar)


main()