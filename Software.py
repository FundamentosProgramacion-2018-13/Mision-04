#Javier Alexandro Vargas Sánchez A01377718
#Programa que sirve para calcular el repcio final de un producto, tomando en cuenta que exiiste descuento por mayoreo

#Función que obtiene el número de unidades a comprar, lo clasifica y con base a eso calcula un descuento
def clasificarDescuento(numeroProductos):
    descuento = 0

    if numeroProductos > 0  and numeroProductos < 10:
        descuento = 0
        print("No hay descuento por esa cantidad de productos")
    if numeroProductos >= 10 and numeroProductos < 20:
        descuento = .20
        print("Si compras ese número de unidades te aplicaremos un descuento del 20%")
    if numeroProductos >= 20 and numeroProductos < 50:
        descuento = .30
        print("Si compras ese número de unidades te aplicaremos un descuento del 30%")
    if numeroProductos >= 50 and numeroProductos < 100:
        descuento = .40
        print("Si compras ese número de unidades te aplicaremos un descuento del 40%")
    if numeroProductos >= 100:
        descuento = .50
        print("Si compras ese número de unidades te aplicaremos un descuento del 50%")
    costoSinDescuento = numeroProductos *1500
    descuentoAplicado = ( costoSinDescuento * descuento)
    costoTotal = costoSinDescuento - descuentoAplicado
    return costoTotal


#Función principal
def main():
    numeroProductos = int(input("¿Cuántos paquetes de software planeas comprar?: "))
    if numeroProductos <= 0:
        print("Error, no puedo calcular el precio")
    else:
        costoTotal = clasificarDescuento(numeroProductos)
        print("El costo total sería de: $%.2f" % (costoTotal ))


#Llamada a la función principal
main()