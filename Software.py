#Damián Iván García Ravelo
#A01376354

#Calcula el precio a pagar dependiendo de los paquetes solicitados


def calcularDescuento (numerosDePaquetes):
#Calcula el descuento que se va a hacer usando la función: descuento * precio de unidades * paquetes pedidos

    if numerosDePaquetes >= 1 and numerosDePaquetes < 10:
        return 0

    elif numerosDePaquetes >= 10 and numerosDePaquetes <19 :
        return (numerosDePaquetes * 1500 * .20)

    elif numerosDePaquetes >=20 and numerosDePaquetes < 50 :
        return (numerosDePaquetes * 1500 * .30)

    elif numerosDePaquetes >= 50 and numerosDePaquetes <99 :
        return (numerosDePaquetes * 1500 * .40)

    elif numerosDePaquetes >= 100 :
        return (numerosDePaquetes * 1500 * .50)



def calcularCostoTotal (numerosDePaquetes):
#Calcula el costo total restandole al precio sin descuento el descuento

    costoTotal = numerosDePaquetes * 1500 - calcularDescuento(numerosDePaquetes)
    return costoTotal


def main():
    numeroDePaquetes = int(input("Teclea el número de paquetes a comprar: "))

#Directamente condiciona al programa para no recibir 0
    if numeroDePaquetes <= 0:
        print("ERROR, número no válido")

#Imprime el descuento y el precio final
    descuento = calcularDescuento(numeroDePaquetes)
    print("El descuento recibido es de $", format(descuento, ".2f"))
    precioFinal = calcularCostoTotal(numeroDePaquetes)
    print("El precio final es de $", format(precioFinal,  ".2f"))

main () #Llama a la función principal

