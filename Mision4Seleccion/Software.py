# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que lee el número de paquetes comprados y despliega la cantidad descontada (si la hay)
# y el total a pagar de la compra.


# Determina el descuento aplicado para la cantidad de paquetes introducida además del costo total.
def calcularCanyTotal(paquetes):
    if paquetes >= 100:
        descuento = 50 * 15
        costoTotalPaquetes = (paquetes * (1500 - descuento))
        return costoTotalPaquetes, descuento

    elif paquetes >= 50 & paquetes < 100:
        descuento = 40 * 15
        costoTotalPaquetes = (paquetes * (1500 - descuento))
        return costoTotalPaquetes, descuento

    elif paquetes < 50 & paquetes >= 20:
        descuento = 30 * 15
        costoTotalPaquetes = (paquetes * (1500 - descuento))
        return costoTotalPaquetes, descuento

    elif paquetes < 20 & paquetes >= 10:
        descuento = 20 * 15
        costoTotalPaquetes = (paquetes * (1500 - descuento))
        return costoTotalPaquetes, descuento


def main():

    # Solicita el numero de paquetes ordenados.
    numeroDePaquetes = int(input("Introduce el número de paquetes: "))

    # Determina si el numero de paquetes es contable y notifica al usuario si no es asi.
    if numeroDePaquetes > 0 :
        cantidadDescontada_y_Total_a_Pagar = calcularCanyTotal(numeroDePaquetes)
        print("La costo total de los paquetes es %d$ con un descuento de %d$"%(cantidadDescontada_y_Total_a_Pagar))
    else:
        print("ERROR")
        print("El 0 y números negativos no son aceptados.")
        print("Intentelo nuevamente.")

main()
# corre el programa
