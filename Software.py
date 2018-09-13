# Autor: Humberto Carrillo Gómez
# Descripción: Este programa calcula el descuento y el total a pagar dependiendo la cantidad de paquetes comprados

# Multiplica el precio por el total de paquetes y le resta el descuento correspondiente.
def calcularPago(paquetes,descuento):

    pago = (1500*paquetes)-(1500*paquetes)*descuento
    return pago


# Función principal: resuelve el problema
def main():
    paquetes=int(input("Teclea el número de paquetes comprados: "))
    if paquetes <= 0:
        print()
        print("""Error
        Parece que tecleaste un número que no es válido, por favor intentálo de nuevo""")
    else:
        descuento = 0
        if paquetes < 9:
            descuento = 0
        if paquetes >= 10 and paquetes <= 19:
            descuento = .20
        if paquetes >= 20 and paquetes <= 49:
            descuento = .30
        if paquetes >= 50 and paquetes <= 99:
            descuento = .40
        if paquetes >= 100:
            descuento = .50
        pagoTotal= calcularPago(paquetes, descuento)

        print("El descuento es de: $%.2f" % (paquetes*1500-pagoTotal))
        print("El pago total es de $%.2f" % pagoTotal)


main()