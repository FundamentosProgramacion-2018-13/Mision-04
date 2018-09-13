# Autor: Luis Armando Miranda Alcocer
# Descripción: Se vende un producto por $1500, y acorde a la cantidad superior a 10 se hace descuento.

def calcularDescuento (cantidadComprada):  #Por intervalos, se realiza el cálculo del descuento de cada uno, descontando el 20, 30, 40 o 50 porciento.
    if cantidadComprada >=10 and cantidadComprada <20:
        descuento = cantidadComprada*1500*.20
        return descuento

    if cantidadComprada >= 20 and cantidadComprada < 50:
        descuento = cantidadComprada*1500 * .30
        return descuento

    if cantidadComprada >=50 and cantidadComprada <100:
        descuento = cantidadComprada*1500*.40
        return descuento

    if cantidadComprada >= 100:
        descuento = cantidadComprada*1500 * .50
        return descuento


def main ():
    cantidadComprada = int(input("Teclea la cantidad de paquetes comprados: ")) #Lee la cantidad de paquetes comprados


    if cantidadComprada < 10 and cantidadComprada > 0: #Si es uno o más, siempre hasta llegar a nueve, se cobra sin descuento
        cantidadAPagar = cantidadComprada * 1500.00
        print("El precio a pagar  es de: $ %.2f " % cantidadAPagar)

    if cantidadComprada >=10: #Si es mayor o igual a 10, se puede calcular el descuento
        descuento = calcularDescuento (cantidadComprada) #Se llama a la función
        print ("La  cantidad descontada es: %.2f" %descuento)
        cantidadAPagar = (cantidadComprada*1500)- descuento #Se calcula la cantidad de paquetes comprados, y se realiza el descuento
        print("El precio a pagar es de: $ %.2f " % cantidadAPagar)

    if cantidadComprada <= 0: #Si se teclea un número igual o menor a cero, imprime error
        print ("Error")

main()
