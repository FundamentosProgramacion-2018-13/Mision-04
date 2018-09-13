# Autor: David Isaí López Jaimes      A01748363
# Hace descuento dependiendo de cuantos paquetes se compraron


def calcularTotal(paquetes):                # Esta función lee los paquetes, los multiplica por su precio normal y les hace el descuento correspondiente al numero de paquetes
    if paquetes <= 0:
        print("Error")
    if paquetes < 10:
        total = paquetes * 1500
    if paquetes <= 19:
        total = (paquetes * 1500) * 0.2
        total = (paquetes * 1500) - total
        return total
    if paquetes >= 20 and paquetes <= 49 :
        total = (paquetes * 1500) * 0.3
        total = (paquetes * 1500) - total
        return total
    if paquetes >= 50 and paquetes <= 99 :
        total = (paquetes * 1500) * 0.4
        total = (paquetes * 1500) - total
        return total
    if paquetes >= 100:
        total = (paquetes * 1500) * 0.5
        total = (paquetes * 1500) - total
        return total


def main():           # Aquí leemos y calculamos las funciones anteriores e imprimimos resultados
    cantidadPaquetes = int(input("Teclea el numero de paquetes comprados: "))
    if cantidadPaquetes < 10:
        print("No hay descuento.")

    if cantidadPaquetes <= 19 and cantidadPaquetes >= 10:
        cantidadDescuento = (cantidadPaquetes * 1500) * 0.2
        print("Cantidad descontada: $", cantidadDescuento)

    if cantidadPaquetes >= 20 and cantidadPaquetes <= 49 :
        cantidadDescuento = (cantidadPaquetes * 1500) * 0.3
        print("Cantidad descontada: $", cantidadDescuento)

    if cantidadPaquetes >= 50 and cantidadPaquetes <= 99 :
        cantidadDescuento = (cantidadPaquetes * 1500) * 0.4
        print("Cantidad descontada: $", cantidadDescuento)

    if cantidadPaquetes >= 100:
        cantidadDescuento = (cantidadPaquetes * 1500) * 0.5
        print("Cantidad descontada: $", cantidadDescuento)


    totalPagar = calcularTotal(cantidadPaquetes)
    print("El total a pagar es: $", totalPagar)

main()