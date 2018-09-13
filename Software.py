#Jocelyn López Ortíz A01377451
#Calcular el descuento y total de pago de una compra de software


def calcularTotal(paquetes): #Calcular el total a pagar
    if paquetes <10:
        descuento = 0
    if paquetes >=10 and paquetes <20:
        descuento = .20
    if paquetes >=20 and paquetes <50:
        descuento = .30
    if paquetes >=50 and paquetes <100:
        descuento = .40
    if paquetes >=100:
        descuento = .50

    total = 1500*paquetes - (1500*paquetes*descuento)
    return total


def main():
    cantidadPaquetes = int(input("Número de paquetes a comprar: "))
    total = calcularTotal(cantidadPaquetes)

    print()
    if cantidadPaquetes > 9:
        print("Cantidad descontada: $%.2f" %(1500*cantidadPaquetes-total))
    if cantidadPaquetes > 0:
        print("El total a pagar es: $%.2f" %total)
    if cantidadPaquetes <=0:
        print("Error")


main()