# Oscar Alejandro Torres Maya, A01377686
# Calcular el precio total del software tenga descuento o no

# Función para calcular descuento dependiendo los paquetes
def calcularDescuento(software):
    costo = 1500 * software
    if software < 10:
        return 0
    elif software >= 10 and software <= 19:
        descuento1 = costo * 0.20
        return descuento1
    if software >= 20 and software <= 49:
        descuento2 = costo * 0.30
        return descuento2
    if software >= 50 and software <= 99:
        descuento3 = costo * 0.40
        return descuento3
    if software >= 100:
        descuento4 = costo * 0.50
        return descuento4

# Función principal
def main():
    software = int(input("Cuántos paquetes de software's compraste? "))
    descuento = calcularDescuento(software)
    costoTotal = (1500*software) - descuento
    if software <= 0:
        print("Hubo un error al teclear la cantidad de software")
    if software > 0:
        print("El descuento aplicado fue de: ", descuento)
        print("El costo total de tus paquetes es: ", costoTotal)

# Llamada de función principal
main()