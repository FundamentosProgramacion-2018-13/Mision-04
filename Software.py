# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que lee y muestra el número de paqeuetes comprados y calcula el total a pagar de la compra.


# La siguiente función calcula el descuento dependiendo del número de paquetes comprados.
def calcularDescuento(numeroDePaquetes, subTotal):
    if numeroDePaquetes < 10:
        descuento = 0
        return descuento
    if numeroDePaquetes >= 10 and numeroDePaquetes <= 19:
        descuento = subTotal * .2
        return descuento
    if numeroDePaquetes >= 20 and numeroDePaquetes <= 49:
        descuento = subTotal * .3
        return descuento
    if numeroDePaquetes >= 50 and numeroDePaquetes <= 99:
        descuento = subTotal * .4
        return descuento
    if numeroDePaquetes >= 100:
        descuento = subTotal * .5
        return descuento


# La siguiente función calcula el total de la compra.
def calcularTotal(numeroDePaquetes, subTotal):
    descuento = calcularDescuento(numeroDePaquetes, subTotal)
    total = subTotal - descuento
    return total


# La función principal lee el número de paquetes y determina si el número ingresado es válido o no.
def main():
    numeroDePaquetes = (float(input("Teclea el número de paquetes de software comprados: ")))
    subTotal = (numeroDePaquetes * 1500)

    if numeroDePaquetes > 0:
        total = calcularTotal(numeroDePaquetes, subTotal)
        print("El total a pagar es: %.2f" % total)
    else:
        print("Error")


# Llamada a la función main.
main()