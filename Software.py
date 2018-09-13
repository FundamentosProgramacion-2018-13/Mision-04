# Sebastian Macias - A01376492
# Calcular el costo de paquetes dependiendo de la cantidad


# Calcula el precio, con descuento incluido, dependiendo del número de paquetes
def costoConDescuento(numeroPaquetesComprados):
    if 1 <= numeroPaquetesComprados <= 9:
        return numeroPaquetesComprados * 1500
    else:
        if 10 <= numeroPaquetesComprados <= 19:
            return (numeroPaquetesComprados * 1500) * .80
        else:
            if 20 <= numeroPaquetesComprados <= 49:
                return (numeroPaquetesComprados * 1500) * .70
            else:
                if 50 <= numeroPaquetesComprados <= 99:
                    return (numeroPaquetesComprados * 1500) * .60
                else:
                    if 100 <= numeroPaquetesComprados:
                        return (numeroPaquetesComprados * 1500) * .50


# Calcula el descuento que se le hará al cliente
def descuentoTotal(numeroPaquetesComprados):
    if 1 <= numeroPaquetesComprados <= 9:
        return "Sin descuento"
    else:
        if 10 <= numeroPaquetesComprados <= 19:
            return (numeroPaquetesComprados * 1500) * .20
        else:
            if 20 <= numeroPaquetesComprados <= 49:
                return (numeroPaquetesComprados * 1500) * .30
            else:
                if 50 <= numeroPaquetesComprados <= 99:
                    return (numeroPaquetesComprados * 1500) * .40
                else:
                    if 100 <= numeroPaquetesComprados:
                        return (numeroPaquetesComprados * 1500) * .50



# Pide el número de paquetes a comprar e imprime los resultados.
def main():
    print("")
    numeroPaquetesComprados = int(input("Introduzca el número de paquetes a comprar: "))
    costoDescontado = costoConDescuento(numeroPaquetesComprados)
    descuento = descuentoTotal(numeroPaquetesComprados)

    if numeroPaquetesComprados <= 0:
        print("ERROR")

    if numeroPaquetesComprados >= 1:
        print("")
        print("Su descuento es de: $ %.2f" % descuento)
        print("Su tota a pagar es de: $ %.2f" % costoDescontado)



main()
