#Autor: Alan Diaz Carrera
#Descripcion: Calcular cuanto se tendra que pagar por lo paquetes comprados

def descontar(paquetes, descuento):
    if paquetes >= 10 and paquetes <= 19:
        descuento = 0.2
        return descuento
    if paquetes >= 20 and paquetes <= 49:
        descuento = 0.3
        return descuento
    if paquetes >= 50 and paquetes <= 99:
        descuento = 0.4
        return descuento
    if paquetes >= 100:
        descuento = 0.5
        return descuento
    
def main():
    descuento=0
    paquetes = int(input("Cantidad de paquetes: "))
    if paquetes <= 0:
        print("Error")
    else:
        descuentos = descontar(paquetes, descuento)
        descuento = 1500*descuentos
        pago = 1500-descuento
        print("El descuenco es: $", descuento)
        print("El pago total es: $", pago)

main()
