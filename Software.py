# Author: Ivan Honc Ayón     A01376466       Grupo 02
# Descripción: Este programa calcula el descuento y el total a pagar de una compra.


# Esta función recibe el número de paquetes comprados y determina que porcentaje de descuento
# debe ser aplicdo, regresa el descuento.
def calcularDescuento(paquetesComprados):
    if paquetesComprados<1:
        strDescuento = "Error: No se ingresó una cantidad correcta."
    if paquetesComprados>0 and paquetesComprados<9:
        descuento = 0
        strDescuento = "El descuento realizado es de "+str(descuento)+"%"
    if paquetesComprados>9 and paquetesComprados<20:
        descuento = 20
        strDescuento = "El descuento realizado es de "+str(descuento)+"%"
    if paquetesComprados>19 and paquetesComprados<50:
        descuento = 30
        strDescuento = "El descuento realizado es de "+str(descuento)+"%"
    if paquetesComprados>49 and paquetesComprados<100:
        descuento = 40
        strDescuento = "El descuento realizado es de "+str(descuento)+"%"
    if paquetesComprados>99:
        descuento = 50
        strDescuento = "El descuento realizado es de "+str(descuento)+"%"

    return strDescuento


# Esta función recibe el número de paquetes comprados y aplica los descuentos correspondientes,
# regresa una cadena con el total.
def calcularTotal(paquetesComprados):
    paquetes = float(paquetesComprados)
    if paquetesComprados<1:
        strTotal = "Error: No se ingresó una cantidad correcta."
    if paquetesComprados>0 and paquetesComprados<9:
        total = 1500*paquetes
        strTotal = "El total a pagar es de: $"+str(total)
    if paquetesComprados>9 and paquetesComprados<20:
        total = 1500 * paquetes * 0.8
        strTotal = "El total a pagar es de: $" + str(total)
    if paquetesComprados>19 and paquetesComprados<50:
        total = 1500 * paquetes * 0.7
        strTotal = "El total a pagar es de: $" + str(total)
    if paquetesComprados>49 and paquetesComprados<100:
        total = 1500 * paquetes * 0.6
        strTotal = "El total a pagar es de: $" + str(total)
    if paquetesComprados>99:
        total = 1500 * paquetes * 0.5
        strTotal = "El total a pagar es de: $" + str(total)

    return strTotal


# Esta es la función principal que recibe los valores del usuario, manda a llamar a las otras funciones,
# e imprime el descuento aplicado y el total a pagar.
def main():
    paquetesComprados = int(input("Teclea en número de paquetes comprados: "))
    descuento = calcularDescuento(paquetesComprados)
    total = calcularTotal(paquetesComprados)

    print("""
%s
%s""" % (descuento, total))


main()
