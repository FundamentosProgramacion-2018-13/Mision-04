#Mariana Caballero Cabrera  A01376544

# Programa que calcule el precio de software aplicando un descuento dependiendo de las unidades que se compren

#Calcula el descuento dependiendo de las unidades compradas

def calcularDescuento(unidades):
    descuento = 0

    if unidades < 10:
        descuento = 0

    else:

        if unidades >= 10:
            descuento = unidades * 1500 * .20


        else:

            if unidades >= 20:
                descuento = unidades * 1500 * .30

            else:

                if unidades >= 50:
                    descuento = unidades * 1500 * .40

                else:
                    if unidades >= 100:
                        descuento = unidades*1500*.50
    return descuento



#Función princpal

def main():

    unidades = int(input("Teclea número de paquetes: "))


    if unidades > 0:
        precio = unidades * 1500
        descuento = calcularDescuento(unidades)
        costoTotal = precio - descuento
        print ("El costo es de: $%.2f" % (precio))
        print ("Con un descuento de: $%.2f" %(descuento))
        print ("Queda un total de: $%.2f" % (costoTotal))
    else:
        print ("Error, no puedo calcular")


# llamamos a la función principal
main()