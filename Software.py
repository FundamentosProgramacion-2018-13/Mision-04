#Autor: David Rodriguez
#Lee el número de paquetes comprados, la cantidad descontada si es que la hay y el total a pagar


#Calcula el porcentaje a descontar
def calcularDescuento(paquetes):
    if paquetes <= 0:
        descuento = 0
    elif 10 <= paquetes <= 19:
        descuento = 0.2
    elif 20 <= paquetes <= 49:
        descuento = 0.3
    elif 50 <= paquetes <= 99:
        descuento = 0.4
    elif 100 <= paquetes:
        descuento = 0.5
    return descuento

#Calcula la cantidad descontada
def cantidadDescontada1 (paquetes, descuento):
    subtotal = paquetes*1500
    cantidadDescontada = subtotal*descuento
    return cantidadDescontada


#Determina so los valores son válidos y calcula el total a pagar en base a los precios originales
def calcularTotal(paquetes, descuento):
    if paquetes <= 0:
        total = "Error"
    else:
        subtotal = paquetes*1500
        cantidadDescontada = subtotal*descuento
        total = subtotal - cantidadDescontada
    return total


#Función principal
def main():
    paquetes = int(input("Dame la cantidad de paquetes comprados: "))
    descuento = calcularDescuento(paquetes)
    cantidadDescontada = cantidadDescontada1(paquetes, descuento)
    total = calcularTotal(paquetes, descuento)
    if total == "Error":
        print(total)
    else:
        print("Paquetes comprados: ", (paquetes))
        print("Cantidad descontada: ", (cantidadDescontada))
        print("Total: ", (total))


main()