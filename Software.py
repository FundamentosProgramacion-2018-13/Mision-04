# Autor: Erick David Ramírez Martínez, A01748155
"""Descripción, programa que lee el número de paquetes comprados de un software y con base a ello
calcula un descuento si existe de los paquetes e imprime el costo total"""


def calcularCosto(paquetes):
    totalParcial = paquetes*1500.00
    if paquetes>0 and paquetes<10:
        totalAPagar = totalParcial
        return totalAPagar
    else:
        if paquetes>=10 and paquetes<=19:
            totalAPagar = totalParcial * .80
            return totalAPagar
        else:
            if paquetes >= 20 and paquetes <= 49:
                totalAPagar = totalParcial * .70
                return totalAPagar
            else:
                if paquetes >= 50 and paquetes <= 99:
                    totalAPagar = totalParcial *.60
                    return totalAPagar
                else:
                    if paquetes >= 100:
                        totalAPagar = totalParcial *.50
                        return totalAPagar


def main():
    paquetes = int(input("Número de paquetes comprados: "))
    if paquetes > 0:
      totalAPagar = float(calcularCosto(paquetes))
      print("El total a pagar es de: $%0.2f" % (totalAPagar))
    else:
        print("Error, no se pueden ingresar números negativos ni el 0")


main()

