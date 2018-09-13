# Sebastian Macias - A01376492
# Cambiar formato de 24 horas a 12 horas


# Calcular la hora basándose en el número dado
def cambiarFormato(horas):
    if 0 > horas < 23:
        return "error"
    else:
        if 0 < horas <= 12:
            return horas
        else:
            if 13 <= horas <= 23:
                return (horas - 12)
            else:
                if horas == 0:
                    return 12


# Obtiene los número para calcular la hora.
# Decir, deoendiendo del resultado regresado, si pertenece en la mañana o tarde.
def main():
    print("")
    horas = int(input("Introducir la hora: "))
    minutos = int(input("introducir los minutos: "))
    segundos = int(input("Introducir los segundos: "))

    horasCambiadas = cambiarFormato(horas)
    print("")
    if horasCambiadas == 1 and horas == 1:
        print("Es la ", horasCambiadas, "con", minutos, "minutos y ", segundos, "segundos de la mañana")
    else:
        if horasCambiadas == 1 and 13 == horas:
            print("Es la ", horasCambiadas, "con", minutos, "minutos y ", segundos, "segundos de la tarde")
        else:
            if horasCambiadas > 1 and 12 <= horas <= 23:
                print("Son las ", horasCambiadas, "con", minutos, "minutos y ", segundos, "segundos de la tarde")
            else:
                if horasCambiadas > 1 and 0 <= horas <= 11:
                    print("Son las ", horasCambiadas, "con", minutos, "minutos y ", segundos, "segundos de la mañana")





main()
