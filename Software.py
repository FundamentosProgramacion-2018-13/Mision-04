#Autor: Jose Luis Mata Lomelí
#Lee el número de paquetes comprados y despliega la cantidad a pagarsegún la tabla dada

costo = 1500

def Descuentado(cantidad):

    if cantidad >=10 and cantidad <=19:
        descuento2 = costo*.20
        return descuento2

    if cantidad >=20 and cantidad <=49:
        descuento3 = costo*.30
        return descuento3

    if cantidad >=50 and cantidad <=99:
        descuento4 = costo*.40
        return descuento4

    if cantidad >= 100:
        descuento5 = costo*.50
        return descuento5


    if cantidad < 10:
        descuento = 0
        return descuento


def pagoFinal(precioFinal):

    dineroDescuentado = costo - (precioFinal)
    return dineroDescuentado




def main():

    paquetes = int(input("Escriba la cantidad de paquetes que compró: "))
    descuentoFinal = Descuentado(paquetes)
    totalPagar = pagoFinal(descuentoFinal)

    print(" ")

    print("Se le descontaran $ %d"% (descuentoFinal))
    print("El total a pagar sera de %d" % (totalPagar))

main()
