# Alex Serrano Durán
# Este programa convierte la hora de formato de 24 hrs a 12 hrs


def convertirA12(horas24):          # Esta función convierte las horas al formato de 12 al
    horas12 = horas24 % 12          # usar el residuo de una división entre 12
    if horas12 == 0:
        horas12 = 12
    return horas12


def main():
    horas24 = int(input("Teclea las horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    horas12 = convertirA12(horas24)

    if 0 < horas24 < 24 and 0 < minutos < 60 and 0 < segundos < 60:
        print("La hora en formato de 12 horas es: %02d:%02d:%02d" % (horas12, minutos, segundos))
    else:
        print("Error")


main()
