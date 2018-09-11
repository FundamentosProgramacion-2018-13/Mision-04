#Autor Claudio Mayoral García
#Lee la cantidad de paquetes comprados y despliega el porcentaje de descuento (si lo hay)
#Y el total de pagar de la compra y si ponen 0 o valores negativos manda un mensaje de error


#Calcula el porcentaje de descuento dependiendo del numero de copias vendidas y regresa el descuento si es que existe
def calcularDescuento(numeroCopias):
    descuento = 0
    if numeroCopias > 0 and numeroCopias < 10:
        descuento = 0
    if numeroCopias >= 10 and numeroCopias < 20:
        descuento = 20
        return descuento
    if numeroCopias >= 20 and numeroCopias < 49:
        descuento = 30
        return descuento
    if numeroCopias >= 50 and numeroCopias < 99:
        descuento = 40
        return descuento
    if numeroCopias >= 100:
        descuento = 50
        return descuento


#Función Principal pide el numero de copias vendidas e imprime el descuento (si es que lo hay) y el precio
#Incluyendo el descuento. Pero si no cumple con los requisitos manda un mensaje de error
def main():
    numeroCopias = int(input("Introduce el número de copias que deseas comprar: "))
    if numeroCopias <= 0:
        print("Número de copas no válido")
    descuento = calcularDescuento(numeroCopias)

    if numeroCopias > 0 and numeroCopias < 10:
        print("El precio es: $", 1500 * numeroCopias)
    if numeroCopias >= 10:
        precio = numeroCopias * 1500 - ((numeroCopias * 1500)*(descuento * 0.01))
        print("El descuento es: ", descuento, "%")
        print("El precio es: $%.2f" % precio)


#Llama a la función principal
main()
