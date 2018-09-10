"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998
Descripción: Calcula el descuento que tendrás al ingresar una cantidad determinada de paquetes. Imprimirá el precio final, el descuento, el total con descuento y el subtotal.

"""

#Calcular el descuento  que el cliente obtenrá con base en el número de paquetes y su precio
def calcularDescuento(paquetes, precioPaquetes):
    if paquetes <= 0:
        return "Error"
    if paquetes < 10 and paquetes > 0:
        return precioPaquetes
    if paquetes < 20 and paquetes > 9:
        veinte = precioPaquetes * .2
        return veinte
    if paquetes < 50 and paquetes > 19:
        treinta = precioPaquetes * .3
        return treinta
    if paquetes < 50 and paquetes > 19:
        cuarenta = precioPaquetes * 4
        return cuarenta
    else:
        cincuenta = precioPaquetes * .5
        return cincuenta


#Define la cantidad de descuento que tendrá el cliente
def definirDescuento(paquetes):
    if paquetes <= 0:
        return "Error"
    if paquetes < 10 and paquetes > 0:
        return "0%"
    if paquetes < 20 and paquetes > 9:
        return "20%"
    if paquetes < 50 and paquetes > 19:
        return "30%"
    if paquetes < 50 and paquetes > 19:
        return "40%"
    else:
        return "50%"

#Calcula el total a pagar con base a el número de paquetes y su costo total
def calcularTotal(paquetes, precioPaquetes):
    if paquetes < 0:
        return "Error"
    if paquetes < 10 and paquetes >= 0:
        return precioPaquetes
    if paquetes < 20 and paquetes > 9:
        veinte = precioPaquetes*.8
        return veinte
    if paquetes < 50 and paquetes > 19:
        treinta = precioPaquetes*.7
        return treinta
    if paquetes < 50 and paquetes > 19:
        cuarenta = precioPaquetes*6
        return cuarenta
    else:
        cincuenta = precioPaquetes*.5
        return cincuenta


#Imprime el subtotal, descuento, el descuento en dinero y la cantidad total a pagar
def imprimir(paquetes, precioPaquetes):
    print("Subtotal: $%.2f" % precioPaquetes)
    print("Descuento: {}" .format(definirDescuento(paquetes)) )
    print("Descontado: {}" .format(calcularDescuento(paquetes, precioPaquetes)))
    print("Total: ${}" .format(calcularTotal(paquetes, precioPaquetes)))


#Agrupa las funciones anteriores para resolver el problema con la función principal
def main():
    paquetes = int(input("Número de paquetes: "))
    precioPaquetes = paquetes*1500
    precioFinal = calcularDescuento(paquetes, precioPaquetes)
    imprimir(paquetes, precioPaquetes)


#Llama a la función principal para resolver el problema
main()