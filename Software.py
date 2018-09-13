#Joshua Sánchez Martínez A01274269
#Calcula el costo total de unidades a pagar aplicando un descuento si es necesario


#Calcula el descuento total
def calcularDescuento(unidades):

    descuento = 0
    if unidades <= 9:
        descuento = 1500*0/100
    else:
        if unidades >= 10 and unidades <= 19:
            descuento = 1500*20/100
        else:
            if unidades >= 20 and unidades <= 49:
                descuento = 1500*30/100
            else:
                if unidades >= 50 and unidades <= 99:
                    descuento = 1500 * 40 / 100
                else:
                    descuento = 1500*50/100

    descuentoTotal = descuento*unidades
    return descuentoTotal


#Función principal
def main ():
    unidadesPorComprar = int(input("Teclea la cantidad de unidades que deseas comprar: "))

    if unidadesPorComprar > 0:
        descuentoTotal = calcularDescuento(unidadesPorComprar)
        costoTotal = 1500*unidadesPorComprar - descuentoTotal
        print("Costo total: $ %.2f" % (costoTotal))
        print("El descuento total fue de: %.2f" % (descuentoTotal))
    else:
        print("Error, no puedo calcular")


#Llamar a la función main
main()