#Autor: Samantha Martínez Franco A01747686
#Calcular el precio de la venta de software dependiendo de las unidades y el descuento que tienen


#función que calcula el valor de los descuentos
def calcularDescuento(unidades):
    pagar=unidades*1500
    if unidades>=10 and unidades<20:
        descuento=pagar*.20
    elif unidades>=20 and unidades<50:
        descuento=pagar*.30
    elif unidades>=50 and unidades<100:
        descuento=pagar*.40
    elif unidades>=100:
        descuento=pagar*.50
    else:
        descuento=pagar*0
    return descuento


#función principal
def main():
    unidades=int(input("¿Cuántas unidades de paquetes vas a querer? "))           #pedir valores
    if unidades<=0:
        print("ERROR valor no valido")                   #error si es negativo o 0
    else:
        descuento=calcularDescuento(unidades)
        pagar=(unidades*1500)-descuento
        if unidades<10:
            print ("No hay descuento ")    #en caso de que sea menos de 10 unidades
            print("El total a pagar es de: $%.2f " % pagar)
        if unidades>=10:
            print("Se le descuenta : $%.2f " % descuento)
            print("El total a pagar es de: $%.2f "% pagar)


main()