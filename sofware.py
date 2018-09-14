# Autor: Danhel Alejandro Mercado
# Este programa se encarga de calular el precio del numero de paquetes

#Esta función se encarga de calcular el descuanto con respecto al numero de paquetes
def calcularDescuento(paquetes, subtotal):
    if paquetes < 10:
        descuento = 0
        return descuento
    elif paquetes >= 10 and paquetes <= 19:
        descuento = subtotal * .2
        return descuento
    elif paquetes >= 20 and paquetes <= 49:
        descuento = subtotal * .3
        return descuento
    elif paquetes >= 50 and paquetes <= 99:
        descuento = subtotal * .4
        return descuento
    elif paquetes >= 100:
        descuento = subtotal * .5
        return descuento

#Esta función se encarga de ontener el total a pagar

def calcularTotal(paquetes, subtotal):
    descuento = calcularDescuento(paquetes, subtotal)
    total = subtotal - descuento
    return total


# Función principal lee datos e imprime resultado

def main():
    paquetes = (float(input("Escribe el numero de paquetes de Sotware a comprar:")))
    subtotal = (paquetes * 1500)
    if paquetes > 0:
        total = calcularTotal(paquetes, subtotal)
        print("Total a pagar es de : %.2f" % total)
    else:
        print ("error")

# Llamar main
main()
