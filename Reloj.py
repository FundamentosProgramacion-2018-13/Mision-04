# Autor: Erick David Ramírez Martínez, A01748155
"""Descripción, programa que lee las horas, los minutos y los segundos de un reloj de 24 horas y
los convierte a formato de 12 horas"""


def convertirFormatoReloj(horas24horas, minutos24horas, segundos24horas):
    if minutos24horas >= 0 and minutos24horas<=59 and segundos24horas >= 0 and segundos24horas<=59:
        if horas24horas < 12 and horas24horas >= 0:
            horas12horas = horas24horas
            minutos12horas = minutos24horas
            segundos12horas = segundos24horas
            reloj12horas = str("%d"%(horas12horas) + ":%02d"%(minutos12horas) + ":%02d"%(segundos12horas) + "am")
            return reloj12horas
        else:
            if horas24horas >= 12 and horas24horas <= 23:
                if horas24horas == 12:
                   horas12horas = horas24horas
                else:
                    horas12horas = horas24horas - 12
                minutos12horas = minutos24horas
                segundos12horas = segundos24horas
                reloj12horas = str("%d" % (horas12horas) + ":%02d" % (minutos12horas) + ":%02d" % (segundos12horas) + "pm")
                return reloj12horas
            else:
                return "Error, hora no válida"
    else:
        return "Error, hora no válida"



def main():
    horas24horas = int(input("Horas en formato de 24 horas: "))
    minutos24horas = int(input("minutos en formato de 24 horas: "))
    segundos24horas = int(input("seundos en formato de 24 horas: "))

    reloj12Horas = convertirFormatoReloj(horas24horas,minutos24horas,segundos24horas)

    print("El reloj de 12 horas indica que son: ", reloj12Horas)


main()