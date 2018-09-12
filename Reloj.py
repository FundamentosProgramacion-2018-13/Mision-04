#Autor: Jesús Zabdiel Sánchez Chávez
#Descripción: Convierte la hora del formato 24 hrs a 12

def convertirHora (hora, minutos, segundos):
    if hora >= 0 and hora <= 23 and minutos >= 0 and minutos <60 and segundos >=0 and segundos <60:
        if hora != 00 and hora != 12:
            formato12Horas = hora - 12
            hora12Horas = "La hora es: %02d:%02d:%02d" % (formato12Horas,minutos,segundos)
            return hora12Horas
        if hora == 0:
            formato12Horas = 12
            hora12Horas = "La hora es: %02d:%02d:%02d" % (formato12Horas,minutos,segundos)
            return hora12Horas
        if hora == 12:
            formato12Horas = 12
            hora12Horas = "La hora es: %02d:%02d:%02d" % (formato12Horas,minutos,segundos)
            return hora12Horas
    else:
        return "Error, hora inválida"



def main():
    hora = int(input("Inserte la hora en formato 24hrs: "))
    minutos = int(input("Inserte los minutos: "))
    segundos = int(input("Inse.rte los segundos"))
    print (convertirHora(hora, minutos, segundos))


main()