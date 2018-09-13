# Autor: Carlos Alberto Reyes Ortiz
# Te da el total a pagar y el descuento que obtendras dependiendo de la cantidad de paquetes comprados



def calcularTotal_a_Pagar(cantidadDePaquetes): #Tomando el descuento y el costo, te da la cantidad total a pagar
    descuento = calcularCantidadDescontada(cantidadDePaquetes)
    total_a_Pagar = 1500 * cantidadDePaquetes - descuento
    return total_a_Pagar



def calcularCantidadDescontada(cantidadDePaquetes):  #Te dice cuanto descuento obtendras dependiendo la cantidad de
                                                     #paquetes comprados
    if cantidadDePaquetes <= 9 and cantidadDePaquetes >= 1:
        return 0
    if cantidadDePaquetes >= 10 and cantidadDePaquetes <= 19:
        return (1500 * cantidadDePaquetes) * .2
    if cantidadDePaquetes >= 20 and cantidadDePaquetes <= 49:
        return (1500 * cantidadDePaquetes) * .3
    if cantidadDePaquetes >= 50 and cantidadDePaquetes <= 99:
        return (1500 * cantidadDePaquetes) * .4
    if cantidadDePaquetes >= 100:
        return (1500 * cantidadDePaquetes) * .5
    if cantidadDePaquetes >= 0 :
        return 0




def main(): #Función principal: Te dice cuanto hubieras pagado sin descuento, cuanto se te descuenta
                              # y cuanto es el total a pagar ya con el descuento
    cantidadDePaquetes = int(input("Escribe la cantidad de paquetes comprados: "))
    print()
    if cantidadDePaquetes >= 1:
        print("Pago normal: $%.2f"  %(1500 * cantidadDePaquetes) )
        descuento = calcularCantidadDescontada(cantidadDePaquetes)
        print("Descuento:   $%.2f" %(descuento))
        print("-----------------------")
        total_a_Pagar = calcularTotal_a_Pagar(cantidadDePaquetes)
        print("Pago total:  $%.2f" %(total_a_Pagar))
    else: print(""" "ERROR" es posible que haya tecleado un núemro negativo o el número 0.
         Favor de introducir una cantidad válida""""")








#Llama la función
main()
