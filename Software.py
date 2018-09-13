#Irma Gomez Carmona, A01747743
#Calcular el total a pagar segun los paquetes requeridos, y aplicar el descuento

def calcularSubtotal(numPaquetes):  #El producto de el numero de paquetes por el precio unitario para obtener el subtotal
    subtotal=numPaquetes*1500
    return subtotal


def calcularDescuento(numPaquetes, subtotal):  #Calcular el descuento conforme al número de paquetes
    if numPaquetes>0 and numPaquetes<=9:
        descuento=0
    elif numPaquetes>=10 and numPaquetes<=19:
        descuento=subtotal*0.2
    elif numPaquetes>=20 and numPaquetes<=49:
        descuento=subtotal*0.3
    elif numPaquetes>=50 and numPaquetes<=99:
        descuento=subtotal*0.4
    elif numPaquetes>=100:
        descuento=subtotal*0.5
    return descuento


def calcularTotal(subtotal,descuento): #Restar el correspondiente descuento al subtotal
    total=subtotal-descuento
    return total


def main (): #Obtener valores, llamar a las otras funciones y mostrar resultados
    numPaquetes=int(input("No. de Paquetes de Software: "))

    if numPaquetes>10:
        subtotal=calcularSubtotal(numPaquetes)
        descuento=calcularDescuento(numPaquetes,subtotal)
        costoTotal=calcularTotal(subtotal,descuento)

        print("------------------------")
        print("Subtotal: $", subtotal)
        print("Descuento: $",descuento)
        print("Total a pagar: $", costoTotal)
    else:
        print("Error")

main ()