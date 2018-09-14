# Autor: Luis Humberto Burgueño Paz
# Lee el número de paquetes comprados y despliega la cantidad descontada (si hay) y el total de la compra


# Recibe la cantidad de paquetes y regresa el descuento
def calcularDescuento(cantidadPaquetes):
    if cantidadPaquetes > 0 and cantidadPaquetes < 10:
        return 0
    else:
        if cantidadPaquetes > 9 and cantidadPaquetes < 20:
            return 0.20
        if cantidadPaquetes > 19 and cantidadPaquetes < 50:
            return 0.30
        if cantidadPaquetes > 49 and cantidadPaquetes < 100:
            return 0.40
        if cantidadPaquetes > 99:
            return 0.50


# Recibe el subtotal y el descuento y regresa la cantidad descontada
def calcularCantidadDescontada(subtotal, descuento):
    cantidadDescontada = subtotal * descuento
    return cantidadDescontada


# Recibe el subtotal y la cantidad descontada y regresa el total a pagar
def calcularTotal(subtotal, cantidadDescontada):
    total = subtotal - cantidadDescontada
    return total


#Función Principal: Lee la cantidad de paquetes y llama a las otras funciones para imprimir los resultados.
def main():
    cantidadPaquetes = int(input("Ingresa el número de paquetes que quieres comprar: "))
    if cantidadPaquetes <= 0:
        print("Error")
    else:
        descuento = calcularDescuento(cantidadPaquetes)
        subtotal = cantidadPaquetes*1500
        cantidadDescontada = calcularCantidadDescontada(subtotal, descuento)
        total = calcularTotal(subtotal, cantidadDescontada)
        print("Cantidad Descontada:", cantidadDescontada)
        print("El total a pagar es:", total)


main()