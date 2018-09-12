#Autor: Jesús Zabdiel Sánchez Chávez
#Descripción: Lee el número  de paquetes comprados de un software y calcula el total a pagar y cantidad descontada
#Dependiendo si hay descuento o no


def calcularTotal (numeroPaquetes):
    if numeroPaquetes < 10:
        totalPagar = numeroPaquetes * 1500
        resultado = "Total a pagar: %d , NO aplica descuento" % (totalPagar)
        return resultado

    elif numeroPaquetes >= 10 and numeroPaquetes < 20:
        totalPagar = numeroPaquetes * (1500*.8)
        resultado = "Total a pagar: %d Con descuento del %s" % (totalPagar, "20%")
        return resultado

    elif numeroPaquetes >= 20 and numeroPaquetes <50:
        totalPagar = numeroPaquetes * numeroPaquetes * (1500*.7)
        resultado = "Total a pagar: %d Con descuento del %s" % (totalPagar, "30%")
        return resultado

    elif numeroPaquetes >=50 and numeroPaquetes <100:
        totalPagar =  numeroPaquetes * (1500*.6)
        resultado = "Total a pagar: %d Con descuento del %s" % (totalPagar,"40%")
        return resultado

    else:
        totalPagar =  numeroPaquetes * (750)
        resultado = "Total a pagar: %d Con descuento del %s" % (totalPagar, "50%")
        return  resultado


def main ():
    numeroPaquetes = int(input("¿Cuántos paquetes deseas comprar?: "))
    if numeroPaquetes > 0:
        print (calcularTotal(numeroPaquetes))

    else:
        print ("Error, valor no válido")

main()

