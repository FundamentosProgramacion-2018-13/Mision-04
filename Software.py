#Emiliano Heredia A01377072
#Calcula el costo total de los paqutes comprados tomando en cuenta la tabla de descuentos

def main():
    flag = True
    while(flag):
        numPaquetes = int(input("Ingrese cantidad de paquetes: "))
        if(checarNumNeg(numPaquetes)):
            pago = calcularPago(numPaquetes)
            print("La cantidad del descuento es de: %.2f"%calcularDesc(numPaquetes))
            print("La cantidad a pagar es la siguiente: %.2f" % pago)
            flag = False
        else:
            print("El numeor ingresado es invalido. Favor de intentar con un valor numerico valido.")


#Verifica que el numero sea mayor a 0
def checarNumNeg(num):
    if(num<1):
        return False
    else:
        return True


#Calcula la cantidad de descuentos
def calcularDesc(paquetes):
    descuento = 0.0
    if(paquetes<10):
        descuento = 0.0
    elif(paquetes<20):
        descuento = 0.2
    elif(paquetes<50):
        descuento = 0.3
    elif(paquetes<100):
        descuento = 0.4
    else:
        descuento = 0.5

    return descuento

#Calcula el costo total de acuerdo al descuento y cantidad de paquetes.
def calcularPago(paquetes):
    return (paquetes * 1500.00) * (1-calcularDesc(paquetes))


main()