#Autor: Luis Mario Cervantes Ortiz
#Descripción: Convertir del formato de 24 hrs al de 12hrs y si no se introduce un valor correcto se manda error


def conversionHorario (horas,minutos,segundos): #Convertir las horas,minutos,segundos en formato 12hrs

    if horas >= 1 and horas < 13 and minutos >= 0 and minutos < 61 and segundos >=0 and segundos < 61:
        return ("Son las: %d:%02d:%02d am " % (horas,minutos,segundos))

    if (horas >= 12 and horas < 24) and (minutos >= 0 and minutos < 61) and (segundos >=0 and segundos < 61):
        horas=horas-12
        return ("Son las: %d:%02d:%02d pm " % (horas,minutos,segundos))
    if horas==0 and minutos >= 0 and minutos < 61 and segundos >=0 and segundos < 61:
        horas=12
        return "Son las: %d:%02d:%02d pm " % (horas,minutos,segundos)
    else:
        return ("ERROR")


def main():#Preguntar los datos

    hora=int(input("¿Que hora es?: "))
    minuto=int(input("¿Con cuàntos minutos? : "))
    segundo=int(input("¿Y cuàntos segundos? :"))

    conversion=conversionHorario(hora,minuto,segundo)

    print(conversion)


main()
