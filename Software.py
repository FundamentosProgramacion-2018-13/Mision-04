#Autor: Alberto Contreras Torres
#El programa leeé el número de paquetes comprados, despliega la cantidad descontada y el total a pagar


#Recibe unidades y regresa pagoTotal
def calculaPagoTotal(unidades):
    if unidades > 0 and unidades < 10:
        precioTotal = 1500
        return precioTotal
    elif unidades >= 10 and unidades < 20:
        precioTotal = 1500 - (1500 * .20)
        return precioTotal
    elif unidades >= 20 and unidades < 50:
        precioTotal = 1500 - (1500 * .30)
        return precioTotal
    elif unidades >= 50 and unidades < 100:
        precioTotal = 1500 - (1500 * .40)
        return precioTotal
    else:
        precioTotal = 1500 - (1500 * .50)
        return precioTotal



def main():
    unidades = int(input("Teclea No. de unidades: "))
    if unidades>0:
        pagoTotal = calculaPagoTotal(unidades)
        print("El pago total es:%.2f "% pagoTotal)
    else:
        print("ERROR")

main()