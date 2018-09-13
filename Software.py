#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripción: Calcula el costo de programas aplicando descuentos


#Calcula el precio multiplicando las unidades que requiere por el precio del paquete menos el descuento
def calcularPrecio(unidades):
    paquete = 1500
    if unidades < 10:
        precio = paquete * unidades
        return precio
    elif unidades >= 10 and unidades <= 19:
        precio = paquete * unidades - ((paquete * unidades) * 0.20)
        return precio
    elif unidades >= 20 and unidades <= 49:
        precio = paquete * unidades - ((paquete * unidades) * 0.30)
        return precio
    elif unidades >= 50 and unidades <= 99:
        precio = paquete * unidades - ((paquete * unidades) * 0.40)
        return precio
    elif unidades >= 100:
        precio = paquete * unidades - ((paquete * unidades) * 0.50)
        return precio

#Calcula el descuento correspondiente
def calcularDescuento(unidades):
    paquete = 1500
    if unidades < 10:
        descuento = ((paquete * unidades) * 0)
        return descuento
    elif unidades >= 10 and unidades <= 19:
        descuento = ((paquete * unidades) * 0.20)
        return descuento
    elif unidades >= 20 and unidades <= 49:
        descuento = ((paquete * unidades) * 0.30)
        return descuento
    elif unidades >= 50 and unidades <= 99:
        descuento = ((paquete * unidades) * 0.40)
        return descuento
    elif unidades >= 100:
        descuento = ((paquete * unidades) * 0.50)
        return descuento



#Función principal
def main():
    unidades = int(input("Ingresa el numero de unidades que deseas comprar: "))
    if unidades > 0:
        calcularPrecio(unidades)
        calcularDescuento(unidades)
        totalprecio = calcularPrecio(unidades)
        totalDescuento = calcularDescuento(unidades)
        print ("")
        print ("La cantidad descontada es de: $%.2f" % (totalDescuento))
        print ("El precio total de la compra es de: $%.2f" % (totalprecio))

    else:
        print ("")
        print ("Error")


main()

