#Autor: Luis Ricardo Chagala Cervantes
#Calcular precio despues de realizar un descuento, dependiendo la cantidad de paquetes a comprar.

def totalPagar(paquetes):
    if paquetes <= 0:
        return "Error."
    if paquetes < 10:
        pagar = paquetes * 1500
        return pagar
    if 10 <= paquetes <= 19:
        pagar = paquetes * 1500
        descuento = pagar * 0.2
        total = pagar - descuento
        return total
    if 20 <= paquetes <= 49:
        pagar = paquetes * 1500
        descuento = pagar * 0.2
        total = pagar - descuento
        return total
    if 50 <= paquetes <= 99:
        pagar = paquetes * 1500
        descuento = pagar * 0.2
        total = pagar - descuento
        return total
    if paquetes >= 100:
        pagar = paquetes * 1500
        descuento = pagar * 0.5
        total = pagar - descuento
        return total


def imprimir(total):
    print("Total a pagar: ", total)


def main():
    paquetes = int(input("Número de paquetes: "))
    total = totalPagar(paquetes)
    imprimir(total)


main()
