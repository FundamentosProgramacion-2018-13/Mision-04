# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Calcula el costo total de compras por mayoreo de software


#Constante del costo
COSTO = 1500


#Calcula el descuento de acuerdo con las unidades adquiridas
def calcularDescuento(unidades):
    if unidades < 10:
        return 0
    if 10 <= unidades <= 19:
        return .2
    if 20 <= unidades <= 49:
        return .3
    if 50 <= unidades <= 99:
        return .4
    if 100 <= unidades:
        return .5


#Calcula el costo total de acuerdo con las unidades adquiridas
def calcularCostoTotal(unidades):
    if 0 < unidades:
        return (COSTO * unidades) * (1-calcularDescuento(unidades))
    return


#Recibe datos e imprime resultados
def main():
    unidades = int(input("Total de unidades compradas: "))
    print("Total a pagar: $%.2f" % (calcularCostoTotal(unidades)))


main()
