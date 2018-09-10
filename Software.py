#Autor: Saúl Figueroa Conde
#Matrícula: A01747306
#Grupo: 02
#Este programa calcula el costo del total de paquetes comprados de una compañía de software, aplicando el descuento
#correspondiente.
#-------------------------------------------------------------------------------------------------------------------

#Esta función recibe como parámetro el valor correspondiente a la cantidad de unidades compradas. Esta función calcula
#el valor del descuento y regresa este mismo valor.
def mostrarDescuento(unidades):

    if unidades >0 and unidades < 10:
        descuento = "0 %"
        return descuento

    elif unidades >= 10 and unidades <= 19:
        descuento = "20 %"
        return descuento

    elif unidades >= 20 and unidades <= 49:
        descuento = "30 %"
        return descuento

    elif unidades >= 50 and unidades <= 99:
        descuento = "40 %"
        return descuento

    elif unidades >= 100:
        descuento = "50 %"
        return descuento

    elif unidades <= 0:
        print("Usted ha ingresado un valor no permitido. Error: intentelo de nuevo.")
        main()


#Esta función recibe como parámetro el valor correspondiente a la cantidad de unidades compradas. Calcula el precio,
#aplicando el descuento correspondiente, y regresa el valor de costo.
def calcularCosto(unidades):
    if unidades < 10:
        costo = 1500
        return costo

    elif unidades >= 10 and unidades <= 19:
        costo = 1500 - (1500 * 0.20)
        return costo

    elif unidades >= 20 and unidades <= 49:
        costo = 1500 - (1500 * 0.30)
        return costo

    elif unidades >= 50 and unidades <= 99:
        costo = 1500 - (1500 * 0.40)
        return costo

    elif unidades >= 100:

        costo = 1500 - (1500 * 0.50)
        return costo


#Se declara la función main. Se le pide al usuario que indique la cantidad de unidades compradas. El valor de las
#unidades se envía a la función calcularCosto y el valor de descuento se envía a mostrarDescuento. Al final, se
#imprime el valor del descuento aplicado, si es que hay, y el costo total de la compra.
def main():

    unidades = int(input("Número de paquetes comprados: "))
    descuento = mostrarDescuento(unidades)
    costo = calcularCosto(unidades)


    print("")
    if descuento == "0 %":
        pass
    else:
        print("Se le ha aplicado un descuento del ", descuento)

    print("---------------------------------------------")
    print("El total de su compra es de: ${:.2f}"  .format(costo))

    print("")
    salir = input("Gracias por haber usado este programa.")
    quit()


#Se llama a la función main. Así corre cada una de las funciones desempeñando la tarea designada para dar solución
#a la problemática planteada.
main()