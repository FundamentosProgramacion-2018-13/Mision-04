# Alex Fernando Leyva Martinez - A01747078 - Grupo: 04
# Calcula el descuento y la cantidad total a pagar dependiendo de la cantidad requerida de paquetes


# Muestra la cantidad descontada dependiendo del número de paquetes
def mostrarDescuento(paquetes):
    porcentaje = 0
    if paquetes < 10:
        porcentaje = 0
        return porcentaje
    elif paquetes >= 10 and paquetes < 20:
        porcentaje = .20
        return porcentaje
    elif paquetes >= 20 and paquetes < 50:
        porcentaje = .30
        return porcentaje
    elif paquetes >= 50 and paquetes < 100:
        porcentaje = .40
        return porcentaje
    elif paquetes >= 100:
        porcentaje = .50
        return porcentaje
    return porcentaje


#Calcular el precio total con respecto al número de paquetes aplicando el descuento
def calcularCosto(paquetes):
    costo = paquetes * 1500
    if paquetes < 10:
        return costo * 1
    elif paquetes >= 10 and paquetes < 20:
        return costo * .80
    elif paquetes  >= 20 and paquetes < 50:
        return costo * .70
    elif paquetes >= 50 and paquetes < 100:
        return costo * .60
    elif paquetes >= 100:
        return costo * .50


# Evalua la cantidad de paquetes para que sea válida e imprime el costo total y la cantidad descontada
def main():
    paquetes = int(input("Cuántos paquetes requieres: "))
    if paquetes > 0:
        costo = calcularCosto(paquetes)
        porcentaje = mostrarDescuento(paquetes)
        porcentajeDescontado = porcentaje*(1500*paquetes)
        print("El costo total es: $%.2f " % costo)
        print("El porcentaje descontado es: $%.2f " % porcentajeDescontado)
    else:
        print("Error")
        main()

        
#Llama la función principal
main()
