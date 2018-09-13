# Autor: Juan Sebastián Lozano Derbez
# Calcula el costo de compra basado en cantidad de unidades

def calcularCosto(unidades):                #Serie de ifs y elses donde se determina la cantidad de descuento y se calcula el total
    if unidades <= 0:
        return "Error"
    else:
        if unidades < 10:
            precio = unidades*1500
            return precio
        else:
            if unidades >= 10 and unidades <= 19:
                precio = (unidades*1500)*0.8
                return precio
            else:
                if unidades >= 20 and unidades <= 49:
                    precio = (unidades * 1500) * 0.7
                    return precio
                else:
                    if unidades >= 50 and unidades <= 99:
                        precio = (unidades * 1500) * 0.6
                        return precio
                    else:
                        if unidades >= 100:
                            precio = (unidades * 1500) * 0.7
                            return precio



def main():                                                         #Se recibe la cantidad de unidades y se imprime. Se imprimen de forma diferente el error y el costo
    unidades = int(input("¿Cuántas unidades desea comprar? "))
    costo = calcularCosto(unidades)
    if costo == "Error":
        print(costo)
    else:
        if costo >= 1:
            print("El costo será de: $", costo)

main()
