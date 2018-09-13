#Autor: Jesús Emmanuel Alcalá Nava
#Descripción: este programa calcula la hora en un formato de 12 horas dada la hora en formato de 24 horas por el usuario

def formato12Horas(hora): #convierte la hora en formato de 12 horas
    if hora == 0:
        return 12
    if hora <= 12:
        return hora
    if hora > 12:
        return hora%12


def mañanaTarde(hora): #regresa si la hora es de la mañana o tarde
    if hora >= 12:
        return "pm"
    return "am"


def main():
    hora = int(input("Hora en formato de 24 horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    horaEn12 = formato12Horas(hora)
    pmAm = mañanaTarde(hora)
    if hora < 0 or hora > 23 or segundos > 59 or segundos < 0 or minutos > 59 or minutos < 0:
        print ("error")
    else:
        print (horaEn12,":",minutos,":",segundos ,pmAm)
main()