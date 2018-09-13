#Jpcelyn López Ortíz A01377451
#Conevrtir la hora en formato de 24 hrs al formato de 12 hrs


def convertirHora(horas, minutos, segundos): #Función para convertir la hora a formato de 12 hrs o descartarla si es inválida
    if minutos>=0 and minutos<60 and segundos>=0 and segundos <60:
        if horas >= 12 and horas<24:
            if horas > 12 and horas < 24:
                horas = horas - 12
            nuevaHora = ("%02d:%02d:%02d pm" % (horas, minutos, segundos))
            return nuevaHora
        if horas>=0 and horas<12:
            if horas == 0:
                horas = 12
            nuevaHora = ("%02d:%02d:%02d am" % (horas, minutos, segundos))
            return nuevaHora
    return "error"


def main():
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    horaNueva = convertirHora(horas, minutos, segundos)

    print(horaNueva)


main()
