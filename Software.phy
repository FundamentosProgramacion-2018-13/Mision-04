#Diego Armando Ayala Hernández

#Matrícula A01376727

#resumen del programa:Pide el numero de paquetes y verifica la cantidad de descuento que da e imprime el costo total

#checa la cantidad de paquetes y hace la operación necesaria dependiendo del descuento que se da
def totalporpagar(numerodepaquetes):
    if numerodepaquetes<=0 :
        return 0
    elif numerodepaquetes >0 and numerodepaquetes<10:
        total=numerodepaquetes*1500
        return total

    elif numerodepaquetes >=10 and numerodepaquetes<20:
        total=numerodepaquetes*1500
        totalcondescuento=total*.8
        return totalcondescuento

    elif numerodepaquetes >19 and numerodepaquetes<50:
        total=numerodepaquetes*1500
        totalcondescuento=total*.7
        return totalcondescuento
    elif numerodepaquetes >49 and numerodepaquetes<100:
        total=numerodepaquetes*1500
        totalcondescuento=total*.6
        return totalcondescuento
    elif numerodepaquetes >99 :
        total=numerodepaquetes*1500
        totalcondescuento=total*.5
        return totalcondescuento
#pide la cantidad de paquetes e imprime el resultado 
def main():
    numerodepaquetes=int(input("Número de paquetes:"))
    total=totalporpagar(numerodepaquetes)
    if total <= 0 :
        print("valor de paquetes invalido ")
    elif total>0:
            print("Total por pagar: $ %.2f"%(total))
