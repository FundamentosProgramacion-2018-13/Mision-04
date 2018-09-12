#Rodolfo Anibal Altamirano Sánchez, A01377949

#Calcula el total a pagar, y la cantidad de software comprado esta dentro de los parametros, se aplica un descuento
def calcularCuenta(comprados):

    if comprados > 0 and comprados <10:
        return comprados*1500
    elif comprados >= 10 and comprados < 20:
        return comprados*1500*0.80
    elif comprados >= 20 and comprados < 50:
        return comprados*1500*0.70
    elif comprados >= 50 and comprados < 100:
        return comprados*1500*0.60
    elif comprados >= 100:
        return comprados*1500*0.50




#Llama la funcion que calcula el total, e imprime ese costo
def main():
    comprados = int(input("Cantdad de paquetes de software comprados: "))

    cuentaConDescuento = calcularCuenta(comprados)
#si la compra es menor o igual a 0 unidades, envia un error
    if comprados <= 0:
        print("Error")

    else:
        print("costo: $%.2f" % cuentaConDescuento)

main()