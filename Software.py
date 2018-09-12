# Alex Serrano Durán
# Este programa recibe los paquetes comprados e indica el total a pagar según los descuentos


def calcularPrecio(cantidadPaquetes):               # La función calcula el precio según los rangos de descuento y la
    precio = 0                                      # cantidad de paquetes
    if 0 < cantidadPaquetes:
        if 0 < cantidadPaquetes <= 9:
            precio = cantidadPaquetes * 1500
            return precio
        if 10 <= cantidadPaquetes <= 19:
            precio = cantidadPaquetes * 1500 * 0.8
            return precio
        if 20 <= cantidadPaquetes < 49:
            precio = cantidadPaquetes * 1500 * 0.7
            return precio
        if 50 <= cantidadPaquetes < 99:
            precio = cantidadPaquetes * 1500 * 0.6
            return precio
        if 100 <= cantidadPaquetes:
            precio = cantidadPaquetes * 1500 * 0.5
            return precio
    return precio


def main():             # Lee la cantidad de paquetes, imprime el precio y el mensaje de error y el descuento si es necesario
    cantidadPaquetes = int(input("Teclea la cantidad de paquetes a comprar: "))
    precio = calcularPrecio(cantidadPaquetes)
    cantidadDescontada = ((cantidadPaquetes * 1500) - precio)
    if cantidadDescontada > 0:
        print("Cantidad descontada: $%d" % cantidadDescontada)
    if precio != 0:
        print("Total a pagar: $%d" % precio)
    else:
        print("Error")

main()
