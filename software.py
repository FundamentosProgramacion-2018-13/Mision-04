#Autor: Jesús Emmanuel Alcalá Nava
#Descripción: este programa pide al usuario la cantidad de paquetes que compró y calcula la cantidad descontada y el total a pagar de acuerdo con la tabla de descuentos


def calcularDescuento(paquetesComprados): #calcula el descuento en bae a los paquetes comprados
 descuento = 0
 if paquetesComprados >= 10 and paquetesComprados <= 19:
        descuento = 0.2
 elif paquetesComprados >= 20 and paquetesComprados <= 49:
        descuento = 0.3
 elif paquetesComprados >= 50 and paquetesComprados <= 99:
        descuento = 0.4
 elif paquetesComprados >= 100:
        descuento = 0.5
 return descuento


def calcularPrecioSinDescuento(paquetesComprados):#calcula el precio original sin el descuento
    precioSinDescuento = paquetesComprados * 1500
    return precioSinDescuento


def calcularCantidadDescontada(paquetesComprados): #calcula la cantidad descontada en base a la tabla
    descuento = calcularDescuento(paquetesComprados)
    cantidadDescontada = calcularPrecioSinDescuento(paquetesComprados) * descuento
    return cantidadDescontada


def calcularTotal(paquetesComprados): #calcula el total a pagar
    cantidadDescontada = calcularCantidadDescontada(paquetesComprados)
    cantidadSinDescuento = calcularPrecioSinDescuento(paquetesComprados)
    total = cantidadSinDescuento - cantidadDescontada
    return total


def main():
    paquetesComprados = int(input("Paquetes comprados:"))
    cantidadDescontada = calcularCantidadDescontada(paquetesComprados)
    total = calcularTotal(paquetesComprados)
    print()
    if paquetesComprados <= 0:
        print("Error")
    elif paquetesComprados <=9:
        print("El total a pagar es: $%.02f" % (total))
    else:
        print("La cantidad descontada es: $%.02f" % (cantidadDescontada))
        print("El total a pagar es: $%.02f" % (total))
main()