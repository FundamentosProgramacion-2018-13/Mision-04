#Arturo Márquez Olivar. A01376086.
#Recibe datos de compra de software de una compañía y te dice cuánto deberás pagar dependiendo de cuántos hayas comprado.


#Se encarga de calcular el total de la cuenta, calculando el descuendo necesario.
def calcularTotal(paquetes):
    if paquetes > 0 and paquetes < 10:
        total = paquetes * 1500
        return total
    else:
        if paquetes >= 10 and paquetes <= 19:
            total = (paquetes * 1500) * .80
            return total
        else:
            if paquetes > 19 and paquetes < 50:
                total = (paquetes * 1500) * .70
                return total
            else:
                if paquetes >= 50 and paquetes <100:
                    total = (paquetes * 1500) * .60
                    return total
                else:
                    if paquetes >= 100:
                        total = (paquetes * 1500) * .50
                        return total


#Es la función que lee los datos y los imprime.
def main():
    paquetes = int(input("¿Cuántos paquetes de software compraste?"))

    total = calcularTotal(paquetes)

    if paquetes <= 0:
        print("Error")
    else:
         print("Si compras %d de paquetes, el total de la cuenta ya con descuento es de: %.2f." % (paquetes, total))


#Llamada a la función main.
main()