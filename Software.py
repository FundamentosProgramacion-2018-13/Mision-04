#Autor: Marco González Elizalde
#Calcula el descuento al comprar un software al mayoreo e imprime el total a pagar


#Calcula la cantidad que se va a descontar de acuerdo a la cantidad que se compra
def calcularDescuento(paquetesComprados):
    cantidadDescontada = 1

    if (19 >= paquetesComprados >= 10):
        cantidadDescontada = 1500.00 * 0.2
        return cantidadDescontada

    if(49 >= paquetesComprados >= 20):
        cantidadDescontada = 1500.00 * 0.3
        return cantidadDescontada

    if(99 >= paquetesComprados >= 50):
        cantidadDescontada = 1500.00 * 0.4
        return cantidadDescontada

    if(paquetesComprados >= 100):
        cantidadDescontada = 1500.00 * 0.5
        return cantidadDescontada

    if(9 >= paquetesComprados >= 1):
        return 0

    #Regresa un valor arbitrario si la cantidad a comprar no es valida
    return 1


#Calcula el total a pagar tomando en cuenta el descuento
def calcularTotal(descuento):

    total = 1500.00 - descuento
    return total


#Programa principal
def main():

    paquetesComprados = int(input("¿Cuántos paquetes va a comprar? "))

    descuento = calcularDescuento(paquetesComprados)
    total = calcularTotal(descuento)

    if (descuento > 1):
        print("""Se descontó $%.02f del monto total.
El monto total a pagar es de: $%.02f""" %(descuento, total))

    if (descuento == 0):
        print("El monto total a pagar es de: $1500.00")

    if (descuento == 1):
        print("Error: Valor no válido")


#Corre el programa principal
main()
