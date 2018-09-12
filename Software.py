#Autor: Diana Marisol Medina Bravo
#Lee el número de paquetes comprados y despliega la cantidad descontada (si la hay) y el total a pagar de la compra.


#Función para calcular el total a pagar
#Recibe la cantidad de paquetes y regresa el total
def calcularTotal(cantidadDePaquetes):

    if cantidadDePaquetes<10:
        totalAPagar=cantidadDePaquetes*1500
        return totalAPagar
    elif cantidadDePaquetes>=10 and cantidadDePaquetes<=19:
        totalAPagar=(cantidadDePaquetes*1500)-(cantidadDePaquetes*1500*0.20)
        return totalAPagar
    elif cantidadDePaquetes>=20 and cantidadDePaquetes<=49:
        totalAPagar=(cantidadDePaquetes*1500)-(cantidadDePaquetes*1500*0.30)
        return totalAPagar
    elif cantidadDePaquetes>=50 and cantidadDePaquetes<=99:
        totalAPagar=(cantidadDePaquetes*1500)-(cantidadDePaquetes*1500*0.40)
        return totalAPagar
    elif cantidadDePaquetes>=100:
        totalAPagar=(cantidadDePaquetes*1500)-(cantidadDePaquetes*1500*0.50)
        return totalAPagar
    else: return "Error"


#Función principal
def main():
    cantidadDePaquetes=int(input("Teclee la cantidad de paquetes: "))
    if cantidadDePaquetes>0:
        pago= calcularTotal(cantidadDePaquetes)
        print("Costo total: $%.2f" % (pago))
    else:
        print("Error")


main()