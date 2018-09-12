#Francisco Ariel Arenas Enciso
#Cálculo del descuetno de una tienda dependiendo del número de artículos comprados


'''
Esta función permite calcular el valor del descuento, es decir, cuanto se reducirá el precio de acuerdo al número de
paquetes comprados que son enviados por la función "main()". Esto último se logra gracias al uso de operadores lógicos
'''
def calcularValor(numero_de_paquetes):
    if numero_de_paquetes >= 1 and numero_de_paquetes < 10:
        return "No hay descuento aplicable"
    if numero_de_paquetes >= 10 and numero_de_paquetes < 19:
        precio = (1500 * 0.2)
        return precio
    if numero_de_paquetes >= 20 and numero_de_paquetes < 49:
        precio = (1500 * 0.3)
        return precio
    if numero_de_paquetes >= 50 and numero_de_paquetes < 99:
        precio = (1500 * 0.4)
        return precio
    if numero_de_paquetes >= 100:
        precio = (1500 * 0.5)
        return precio
    if numero_de_paquetes <= 0:
        return "Error"


'''
Mediante el uso de operaciones arítmeticas, lógicos y relacionales, la función obtiene el precio del número de
paquetes con o sin descuento.
'''
def calcularDescuento(numero_de_paquetes):
    if numero_de_paquetes >= 1 and numero_de_paquetes < 10:
       precio = 1500
       return precio
    elif numero_de_paquetes >= 10 and numero_de_paquetes < 19:
       precio = 1500 - (1500 * 0.2)
       return precio
    elif numero_de_paquetes >= 20 and numero_de_paquetes < 49:
       precio = 1500 - (1500 * 0.3)
       return precio
    elif numero_de_paquetes >= 50 and numero_de_paquetes < 99:
       precio = 1500 - (1500 * 0.4)
       return precio
    elif numero_de_paquetes >= 100:
       precio = 1500 - (1500 * 0.5)
       return precio
    if numero_de_paquetes <= 0:
       return "Error"


'''
Función main, la cual controla todo el programa, envía la cantidad de número de paquetes a la función
"calcularDescuento", así como a la función "calcularValor" e imprime el total a pagar, así como el decuento.
'''
def main():
    numero_de_paquetes = int(input("¿Cuántos paquetes se compraron? "))
    descuento = calcularValor(numero_de_paquetes)
    pagoTotal = calcularDescuento(numero_de_paquetes)
    print("Descuento:", (descuento))
    print("Pago total: ", (pagoTotal))


main()