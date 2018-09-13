#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que determina el descuento aplicado y calcula el total a pagar, dependiendo del número de paquetes comprados.


#Función que determina el descuento, dependiendo del número de paquetes comprados.
def determinarDescuento(paquetesComprados):
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


#Función que calcula la cantidad por pagar, sin aplicar descuento.
def calcularCantidadSinDescuento(paquetesComprados):
    cantidadSinDescuento = paquetesComprados * 1500
    return cantidadSinDescuento


#Función que calcula la cantidad descontada.
def calcularCantidadDescontada(paquetesComprados):
    descuento = determinarDescuento(paquetesComprados)
    cantidadDescontada = calcularCantidadSinDescuento(paquetesComprados) * descuento
    return cantidadDescontada


#Función que calcula el total a pagar, restando la cantidad descontada a la cantidad por pagar sin descuento.
def calcularTotalAPagar(paquetesComprados):
    cantidadDescontada = calcularCantidadDescontada(paquetesComprados)
    cantidadSinDescuento = calcularCantidadSinDescuento(paquetesComprados)
    totalAPagar = cantidadSinDescuento - cantidadDescontada
    return totalAPagar


#Función principal. Lee e imprime datos.
def main():
    paquetesComprados = int(input("¿Cuántos paquetes compró? "))
    cantidadDescontada = calcularCantidadDescontada(paquetesComprados)
    totalAPagar = calcularTotalAPagar(paquetesComprados)

    print()

    if paquetesComprados <= 0:
        print("Error")
    elif paquetesComprados <=9:
        print("El total a pagar es: $%.02f" % (totalAPagar))
    else:
        print("La cantidad descontada es: $%.02f" % (cantidadDescontada))
        print("El total a pagar es: $%.02f" % (totalAPagar))


#Llamar a la función principal
main()