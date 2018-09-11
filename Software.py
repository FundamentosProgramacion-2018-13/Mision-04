#Autor: Alejandro Torices Oliva
#Es un programa que calcula la cantidad descontada y el costo total dependiendo del número
# de paquetes que se desee adquirir.

#calcula el descuento dependiendo del número de paquetes adquiridos.
def calcularDescuento(unidades):
    if unidades < 10:
        return 0
    elif unidades >= 10 and unidades < 20:
        return 0.2
    elif unidades >= 20 and unidades < 50:
        return 0.3
    elif unidades >= 50 and unidades < 100:
        return 0.4
    else:
        return 0.5


#Función principal
def main():
    paquetes = int(input("Ingrese el número de paquetes que desea adquirir: "))
    print(" ")
    if paquetes >0:
        descuento = calcularDescuento(paquetes)
        if descuento == 0:
            total = paquetes*1500
            print("Total: $%.2f" % total)
        else:
            sinDescuento = paquetes*1500
            cantidadDescontada = sinDescuento * descuento
            total = sinDescuento - cantidadDescontada
            print("Descuento: $%.2f" % cantidadDescontada)
            print("Total: $%.2f " % total)
    else:
        print("Error, no puedo calcular.")


main()