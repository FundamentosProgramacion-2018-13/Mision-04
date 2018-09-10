# Autor: Silvia Ferman Muñoz
# Programa que lee el número de paquetes comprados e imprime la cantidad descontada (si la hay) y el total.
# Tecnica Top-Down


# CONSTANTE del costo
costo = 1500


# Calcular el descuento, depende de las unidades
def calcularDescuento(paquetes):
     if paquetes < 10:
         return 0
     if paquetes >= 10 and paquetes <= 19:
         return .2
     if paquetes >= 20 and paquetes <= 49:
         return .3
     if paquetes >= 50 and paquetes <= 99:
         return .4
     if paquetes >= 100:
         return .5


# Calcular el total a pagar
def calcularTotalPagar(paquetes):
    if paquetes > 0:
        return (costo * paquetes) * (calcularDescuento(paquetes))
    else:
         print("ERROR, NO se puede calcular")


# Función principal
def main():
     paquetes = int(input("Los paquetes comprados son: "))
     print("El total a pagar es de: $%.2f" % (calcularTotalPagar(paquetes)))


# Llama a la función principal
main()