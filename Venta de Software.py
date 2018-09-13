# Autor: Ithan Alexis Pérez Sánchez
# Saber la cantidad de paquetes de venta que hace una empresa, en base a su lista de descuentos y el precio a pagar

# El codigo empieza después de esta linea

def cantidad_de_paquetes(Unidades): # Aquí se hace los calculos de los descuentos en base a las unidades y el precio total a pagar
    if Unidades >= 10 and Unidades <= 19:
        return  1500 - (1500 * 0.20)
    else:
        if Unidades >= 20 and Unidades <= 49:
            return 1500 - (1500 * 0.30)
        else:
            if Unidades >= 50 and Unidades <= 99:
                return 1500 - (1500 * 0.40)
            else:
                if Unidades >= 100:
                    return 1500 - (1500 * 0.50)
                else:
                    if Unidades <= 0:
                        return "Error"
    return 1500


def main(): # El valor que nosotros le ponemos para poder saber nuestro precio que tenemos que pagar
    Unidades = int(input("Ingresa las unidades que compraras: "))
    Aviso = cantidad_de_paquetes(Unidades)
    print("Este es el Precio Total: ", Aviso)

main()