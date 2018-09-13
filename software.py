# Autor: Jonathan Sanabria Rocha
# Descripcion: Calcular el total con o sin descuento de los paquetes,
#              si se teclea un numero negativo, imprimir mensaje de error.


def calcularTotalVenta (cantidadPaqeutes):
    if cantidadPaqeutes < 10:
        total = cantidadPaqeutes * 1500
        return total
    elif 10 <= cantidadPaqeutes <= 19:
        total = cantidadPaqeutes * (1500-(1500*0.20))
        return total
    elif 20 <= cantidadPaqeutes <= 49:
        total = cantidadPaqeutes * (1500-(1500*0.30))
        return total
    elif 50 <= cantidadPaqeutes <= 99:
        total = cantidadPaqeutes * (1500-(1500*0.40))
        return total
    else:
        total= cantidadPaqeutes * (1500-(1500*0.50))
        return total


# Funcion Principal
def main():
    paquetesComprados = int(input("Teclea el numero de paquetes que va a comprar: "))
    if 0 < paquetesComprados < 10:
        total= calcularTotalVenta(paquetesComprados)
        print("Total: $", total)
    elif paquetesComprados >= 10:
        total = calcularTotalVenta(paquetesComprados)
        cantidadDescuento = paquetesComprados * 1500 - total
        print("Total: %", total)
        print("Cantidad de descuento: % ", cantidadDescuento)

    else:
        negativosCero = "Error"
        print(negativosCero)



# Llama la funcion principal
main()


