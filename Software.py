#Autor Zabdiel Valentin.
#Calcular el total(con o sin descuento) al comprar software en varias cantidades.

def totalPagar(c):
    if c<=0:
        return "error"
    if c<10:
        total=c*1500
        return total
    if 19>c>=10:
        totalSinDescuento=c*1500
        descuento=totalSinDescuento*0.2
        total=totalSinDescuento-descuento
        return total
    if 49>c>=20:
        totalSinDescuento=c*1500
        descuento=totalSinDescuento*0.3
        total=totalSinDescuento-descuento
        return total
    if 99>c>=50:
        totalSinDescuento=c*1500
        descuento=totalSinDescuento*0.4
        total=totalSinDescuento-descuento
        return total
    if c>=100:
        totalSinDescuento=c*1500
        descuento=totalSinDescuento*0.5
        total=totalSinDescuento-descuento
        return total


def main():
    cantidad=int(input("Teclee el numero de paquetes: "))
    total=totalPagar(cantidad)
    print("Usted pagara: ",total)


main()
