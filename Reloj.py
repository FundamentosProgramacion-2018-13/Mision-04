# Autor: Juan Carlos Flores García, A01376511

# Descripción: Programa que convierte las horas del formato de 24 horas al formato de 12 horas.


# La siguiente función convierte las horas del formato de 24 horas al formato de 12 horas.
def convertirFormatoHorario(horas, minutos, segundos):
    if (0 <= horas <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):

        if horas < 12:
            horas = horas - 12
            return ("%d: %02d: %02d am" % (horas, minutos, segundos))
        else:
            return ("%d: %02d: %02d pm" % (horas, minutos, segundos))

    else:
        return ("Error")


# La función principal lee los valores de horas, minutos y segundos además de imprimir las horas en el formato de 12.
def main ():

    horas = int(input("Teclea las horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    print(convertirFormatoHorario(horas, minutos, segundos))

#Llamada a la funcion main.
main()