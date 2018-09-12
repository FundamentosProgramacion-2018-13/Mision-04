#Mariana Caballero Cabrera  A01376544




def calcularHora (hora):

    if hora >=0 and hora<=12:
        horaFormato = hora

    elif hora>=13 and hora <=24:
        horaFormato = hora - 12

    return horaFormato


def main ():

    hora = int(input("Hora: "))
    minuto = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    if hora >=0 and hora <=24 and minuto<60 and segundos<60:
        horaFormato = calcularHora(hora)
        print ("Hora: %d:%02d:%02d hrs" % (horaFormato,minuto,segundos))

    else:
        print ("Error")


main()

