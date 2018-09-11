#Autor: Víctor Manuel Rodríguez Loyola
#Conversión de una hora dada en formato de 24 horas al formato de 12 horas


def ConvertirA12Horas(horas, minutos, segundos): #Convierte las hora ingresada por el usuario a formato de 12 horas.
    if horas==0:
        return 12, 'pm'

    if horas >0 and horas <12:
        return horas, 'am'
    else:
        horasEn12Horas = horas - 12
        return horasEn12Horas, 'pm'


def main():
    horasEn24Hrs=int(input("Teclea las horas: "))
    minutosEn24Hrs= int(input("Teclea los minutos: "))
    segundosEn24Hrs=int(input("Teclea los segundos: "))
    horaEn12Hrs= ConvertirA12Horas(horasEn24Hrs, minutosEn24Hrs, segundosEn24Hrs)

    if horasEn24Hrs <0 or horasEn24Hrs >23 or minutosEn24Hrs <0 or minutosEn24Hrs >60 or segundosEn24Hrs<0 or minutosEn24Hrs>60:
        print("Error. Inténtalo de nuevo")
    else:
        print("La hora en formato de 12 horas es: %d:%02d:%02d %s." %(horaEn12Hrs[0],minutosEn24Hrs,segundosEn24Hrs,horaEn12Hrs[1]))


main()
