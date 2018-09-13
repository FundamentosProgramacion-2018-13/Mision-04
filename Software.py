#Autor Luis Mario Cervantes Ortiz
#Descripción: Mostrar el costo del número de paquetes comprados y si se llega a comprar una cierta cantidad mostrar el costo con el descuento


def paquetes(numeropack): #Saber el costo de cada paquete y saber cuanto tendra de descuento
    if numeropack>10 and numeropack<0:
        totalpack= numeropack*1500
        return totalpack
    else:
        if numeropack >= 10 and numeropack <=19:
            totalpack= numeropack*(1500*.80)
            return totalpack
        else:
            if numeropack >= 20 and numeropack <=49:
                totalpack=numeropack*(1500*.70)
                return totalpack
            else:
                if numeropack >= 50 and numeropack <= 99:
                    totalpack = numeropack * (1500 * .60)
                    return totalpack
                else:
                    if numeropack >= 10:
                        totalpack = numeropack * (1500 * .50)
                        return totalpack
                    else:
                        return "Error"


def main():
    numeropaquetes=int(input("¿Cuaántos paquetes compraste?: "))
    pagopaquetes= paquetes(numeropaquetes)
    print("Total a pagar es de: ",pagopaquetes)

main()