# Autor: Rubén Villalpando Bremont
# El programa calcula el total de la compra, el número de paquetes comprados y el descuanto aplicado a ellos.


# Calcula el precio total con el descuento aplicado a partir del número de paquetes comprados
def calcularPrecio(cantidadDePaquetes):
    if cantidadDePaquetes < 10:
        precioTotal = cantidadDePaquetes*1500
        return precioTotal
    elif 10 <= cantidadDePaquetes <= 19:
        precioTotal = cantidadDePaquetes * (1500*0.8)
        return precioTotal
    elif 20 <= cantidadDePaquetes <= 49:
        precioTotal = cantidadDePaquetes * (1500*0.7)
        return precioTotal
    elif 50 <= cantidadDePaquetes <= 99:
        precioTotal = cantidadDePaquetes * (1500*0.6)
        return precioTotal
    else:
        precioTotal = cantidadDePaquetes * (1500*0.5)
        return precioTotal


# Función Principal
def main():
    paquetesComprados = int(input("Escribe el número de paquetes que le vas a comprar a la compañía: "))
    if 0 < paquetesComprados < 10:
        precioTotal = calcularPrecio(paquetesComprados)
        print("Total a pagar: $", precioTotal)
    elif paquetesComprados >= 10:
        precioTotal = calcularPrecio(paquetesComprados)
        descuento = paquetesComprados * 1500 - precioTotal
        print("Total a pagar: $", precioTotal)
        print("Cantidad descontada: $", descuento)
    else:
        print("Error, el número de paquetes a comprar tiene que ser mayor a cero.")

# Llamar a main
main()

