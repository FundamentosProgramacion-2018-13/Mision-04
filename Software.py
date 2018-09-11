# Autor Daniel Cordova Bermudez
# Grupo 02
# Descripcion:El programa calcula el costo de comprar paquetes de Software los cuales tienen diferentes descuentos, que se calculan dependiendo de la compra.

#Función calcularDescuento se encarga de dar el descuento correcto al usuario comparando con la cantidad paquetes que se desean comprar,

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


#Función calcularTotal calcula el total de la compra.
    
def calcularTotal(numeroPaquetes, subTotal):

    descuento = calcularDescuento(numeroPaquetes,subTotal)
    total = subTotal - descuento
    return total


#Función principal donde se pide la cantidad de paqutes, se verifica si es correto además de imprimir los resultados.

def main():
    numeroPaquetes = (float(input("Escribe el numero de paquetes de Sotware a comprar:")))
    subTotal = (numeroPaquetes * 1500)

    if numeroPaquetes > 0:
        total = calcularTotal(numeroPaquetes, subTotal)
        print("Total a pagar es de : %.2f" % total)
    else:
        print("Error")

#Llamar main

main()
