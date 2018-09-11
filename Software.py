#Autor: Víctor Manuel Rodríguez Loyola
#Cálculo del descuento correspondiente a la compra de X cantidad de paquetes de una compañía de software.


def CalcularSubtotal(paquetes):  #Calcula el total a pagar aplicando el descuento correspondiente a partir de los paquetes comprados.

    if paquetes>0 and paquetes<10:
        subtotal= paquetes*1500
        descuento=0
        return [subtotal,descuento]

    if paquetes>=10 and paquetes <20:
        descuento= paquetes*1500*.20
        subtotal= paquetes*1500-descuento
        return [subtotal,descuento]

    if paquetes>=20 and paquetes <50:
        descuento= paquetes*1500*.30
        subtotal= paquetes*1500-descuento
        return [subtotal,descuento]

    if paquetes>=50 and paquetes<100:
        descuento= paquetes*1500*.40
        subtotal=paquetes*1500-descuento
        return [subtotal,descuento]

    if paquetes >=100:
        descuento= paquetes*1500*.50
        subtotal= paquetes*1500-descuento
        return [subtotal,descuento]



def main():
    paquetesComprados= int(input("¿Cuántos paquetes compraste? "))
    totalAPagar = CalcularSubtotal(paquetesComprados)

    if paquetesComprados<=0:
        print("Error. Inténtalo de nuevo")
    else:

        print("El total a pagar es de: $%.2f Obtuviste un descuento de $%d" %(totalAPagar[0],totalAPagar[1]))


main()
