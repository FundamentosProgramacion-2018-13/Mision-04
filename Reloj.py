# Autor: Rubén Villalpando Bremont
# El programa convierte la hora en formato de 24 horas y la devuelve en formato de 12 horas.


# Convierte la hora del formato de 24 horas y la devuelve en formato de 12 horas
def convertirDe24HorasA12Horas(hora, minuto, segundo):
    if hora >= 12:
        horaActual = ("%.0f:%.0f:%.0f p.m." % (hora % 12, minuto, segundo))
        return horaActual
    else:
        horaActual = ("%.0f:%.0f:%.0f a.m." % (hora % 12, minuto, segundo))
        return horaActual


# Función Principal
def main():
    hora = int(input("Escribe la hora actual: "))
    minuto = int(input("Escribe el minuto actual: "))
    segundo = int(input("Escribe el segundo actual: "))
    if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
        print(convertirDe24HorasA12Horas(hora, minuto, segundo))
    else:
        print("error")

# Llamar a main
main()