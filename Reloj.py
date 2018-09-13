# Carlos Badillo García
# Programa que convierte la hora en formato de 24 horas al formato de 12 hrs.


def convertiraFormato12hrs (hora): # Convertir la hora del formato 24hrs al formato 12hrs
    if hora == 0:
        return 12
    elif hora == 1:
        return 1
    elif hora == 2:
        return 2
    elif hora == 3:
        return 3
    elif hora == 4:
        return 4
    elif hora == 5:
        return 5
    elif hora == 6:
        return 6
    elif hora == 7:
        return 7
    elif hora == 8:
        return 8
    elif hora == 9:
        return 9
    elif hora == 10:
        return 10
    elif hora == 11:
        return 11
    elif hora == 12:
        return 12
    elif hora == 13:
        return 1
    elif hora == 14:
        return 2
    elif hora == 15:
        return 3
    elif hora == 16:
        return 4
    elif hora == 17:
        return 5
    elif hora == 18:
        return 6
    elif hora == 19:
        return 7
    elif hora == 20:
        return 8
    elif hora == 21:
        return 9
    elif hora == 22:
        return 10
    elif hora == 23:
        return 11


def main(): # El usuario introduce la hora, los minutos y los segundos, además se imprime la hora (en formato de 12hrs) si la cantidad ingresada es valida
    hora = int(input("La hora (en formato de 24hrs): "))
    minutos = int(input("Los minutos: "))
    segundos = int(input("Los segundos: "))
    print()
    horaFormato12 = convertiraFormato12hrs(hora)
    if  hora < 0 or hora > 23 or minutos < 0 or minutos > 59 or segundos < 0 or segundos > 59:
        print("Error: hora, minutos o segundos invalidos")
    elif horaFormato12 >= 0 and horaFormato12 <= 11:
        print ("La hora (en fornato de 12hrs) es: %d:%02d:%02d AM" % (horaFormato12, minutos, segundos))
    elif horaFormato12 >= 12 and horaFormato12 <= 23:
        print("La hora (en fornato de 12hrs) es: %d:%02d:%02d PM" % (horaFormato12, minutos, segundos))


main()