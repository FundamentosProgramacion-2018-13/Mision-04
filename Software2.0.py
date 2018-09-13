#Autor: Alberto Contreras Torres
#El programa leeé el número de paquetes comprados, despliega la cantidad descontada y el total a pagar

#Recibe unidades, regresa descuento
def calculaDescuento(unidades):
    if unidades > 0 and unidades < 10:
        descuento = 1500
        return descuento
    elif unidades >= 10 and unidades < 20:
        descuento = (1500 * .20)
        return descuento
    elif unidades >= 20 and unidades < 50:
        descuento = (1500 * .30)
        return descuento
    elif unidades >= 50 and unidades < 100:
        descuento = (1500 * .40)
        return descuento
    else:
        descuento = (1500 * .50)
        return descuento


#Recibe descuento regresa pago total
def calcularPagoTotal(descuento):
    pagoTotal = 1500 - descuento
    return pagoTotal


#Función principal
def imprimir(descuento, pagoTotal, unidades):
    if unidades<0:
        print("ERROR")
    else:
        print("El descuento es = $", descuento)
        print("El pago total es: $", pagoTotal)



def main():
    precioNormal = 1500
    unidades = int(input("Teclea No. de unidades: "))
    descuento = calculaDescuento(unidades)
    pagoTotal = calcularPagoTotal(descuento)
    imprimir(descuento, pagoTotal, unidades)

main()