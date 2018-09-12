# Luis Jonathan Rosas Ramos
# A01377942
# Calcular los descuentos de un software vendido por una empresa, con base en el numero comprado

#definir los el total con los descuentos
def pagarTotal(x):
    # comprar el dato introducido para saber en que rango se encunetre, para aplicar el desceunto correspondiente
    if x < 10 and x > 0:
        total = x*1500
        return total
    elif x >= 10 and x <= 19:
        total = x*(1500*0.8)
        return total
    elif x >= 20 and x <= 49:
        total = x*(1500*0.7)
        return total
    elif x >= 50 and x <= 99:
        total = x*(1500*0.6)
        return total
    elif x >= 100:
        total = x*(1500*0.5)
        return total
    # para el numero igual a 0 o negativos el resultado debe mostrar error o los que no aparecen
    # en el rango de arriba
    else:
        return "Error"

#Funcion principal
def main():
    paquetes = int(input("¿Cuantos paquetes compraste?: "))
    pagoTotal = pagarTotal(paquetes)
    print("El total con descuento es de: ",pagoTotal)

# Llamada funcion principal
main()