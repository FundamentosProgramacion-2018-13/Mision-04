# Autor: Oscar Macias Rodríguez
# Descripción: Lee el número de paquetes comprados y despliega la cantidad descontada(si la hay) y el total a pagar.


# Función principal. Imprime el total a pagar y recibe la cantidad de paquetes.
def main():
    cantidadPaquetes = int(input("Cantidad de paquetes: "))
    print("Total: $", totalPagar(cantidadPaquetes))


# Calcula el precio con descuento.
def totalPagar(cantidadPaquetes):
    precioFijo = 1500

    if 0 >= cantidadPaquetes:
            print("Error")
            main()
    else:
        if 1 <= cantidadPaquetes < 9:
            return(precioFijo)
        if 10 <= cantidadPaquetes < 19:
            return(precioFijo*1.20)
        if 20 <= cantidadPaquetes < 49:
            return(precioFijo*1.30)
        if 50 <= cantidadPaquetes < 99:
            return(precioFijo*1.40)
        if 100 <= cantidadPaquetes:
            return(precioFijo*1.50)
        return


main()