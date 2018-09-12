# Autor: Zoe Caballero Domínguez
# Lee el número de programas comprados, calcula el descuento y muestra la cantidad descontada y el total a pagar.

# La función calcula el costo de los paquetes y el descuento, calculando el total a pagar restandole el descuento
def calcularCostoPaquetes(paquetesComprados):
    precio = paquetesComprados * 1500

    if paquetesComprados > 0 and paquetesComprados < 10:
        descuento = 0
    elif paquetesComprados >= 10 and paquetesComprados <=19:
        descuento = precio * 0.20
    elif paquetesComprados >= 20 and paquetesComprados <= 49:
        descuento = precio * 0.30
    elif paquetesComprados >= 50 and paquetesComprados <=99:
        descuento = precio * 0.40
    else:
        descuento = precio * 0.50

    costoTotal = precio - descuento
    return """El descuento es de: $%.2f 
El costo total es: $%.2f""" % (descuento, costoTotal)


# Función principal
def main():
    paquetesComprados = int(input("Teclea la canctidad de paquetes comprados: "))
    if paquetesComprados > 0:
        print(calcularCostoPaquetes(paquetesComprados))
    else:
        print("Hay un error en la cantidad")


# Llamar a la función
main()