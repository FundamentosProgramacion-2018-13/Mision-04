#Jesús Roberto Herrera Vieyra // A01377230

#Programa para calcular el descuento de la compra

#funcion para calcular el precio por unidad
def calcularPrecio(numeroDeUnidades):
    precio= numeroDeUnidades*1500
    return precio


#funcion para calcular el descuento
def calcularDescuento(numeroDeUnidades, precioNormal):

    if numeroDeUnidades <= 0:
        return "Error"

    if numeroDeUnidades >= 1 and numeroDeUnidades < 10:
        descuento = 0
        return descuento

    if numeroDeUnidades >= 10 and numeroDeUnidades < 20:
        descuento= precioNormal*0.20
        return descuento

    if numeroDeUnidades >= 20 and numeroDeUnidades < 50:
        descuento = precioNormal*0.30
        return descuento

    if numeroDeUnidades >= 50 and numeroDeUnidades < 100:
        descuento= precioNormal*0.40
        return descuento

    if numeroDeUnidades >= 100:
        descuento = precioNormal*0.50
        return descuento


#funcion para calcular el total a pagar
def calcularTotal(descuento,precioNormal):

    if descuento != "Error":
        precioFinal= precioNormal-descuento
        return precioFinal

    else:
        return "Error"


def main():

    numeroDeUnidades= int(input("Teclee el número de unidades vendidas: "))
    precioNormal = calcularPrecio(numeroDeUnidades)
    descuento = calcularDescuento(numeroDeUnidades,precioNormal)
    TotalaPagar = calcularTotal(descuento,precioNormal)

    if descuento != "Error":
        print("Descuento: $%d" %(descuento))
        print("Total a pagar: $%d" %(TotalaPagar))

    else:
        print("ERROR")

main()