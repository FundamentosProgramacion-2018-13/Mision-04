# Autor Daniel Cordova Bermudez
# Grupo 02
# Descripcion:


def calcularDescuento(numeroPaquetes,subTotal):
    if numeroPaquetes < 10:
        descuento= 0
        return descuento
    if numeroPaquetes >= 10 and numeroPaquetes <= 19:
        descuento = subTotal*.2
        return descuento
    if numeroPaquetes >= 20 and numeroPaquetes <= 49:
        descuento = subTotal*.3
        return descuento
    if numeroPaquetes >= 50 and numeroPaquetes <= 99:
        descuento = subTotal*.4
        return descuento
    if numeroPaquetes >= 100:
        descuento = subTotal*.5
        return descuento


def calcularTotal(numeroPaquetes, subTotal):

    descuento = calcularDescuento(numeroPaquetes,subTotal)
    total = subTotal - descuento
    return total




def main():
    numeroPaquetes = (float(input("Escribe el numero de paquetes de Sotware a comprar:")))
    subTotal = (numeroPaquetes * 1500)

    if numeroPaquetes > 0:
        total = calcularTotal(numeroPaquetes, subTotal)
        print("Total a pagar es de : %.2f" % total)
    else:
        print("Error")




main()