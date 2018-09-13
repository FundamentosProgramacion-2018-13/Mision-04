#Autor: Masrco González Elizalde
#Convierte la hora dada de formato de 24 horas al de 12 horas


#Convierte la hora del tiempo dado al formato de 12 horas en una cadena, regresa "Error" si no es una hora valida
def convertirTiempo(hora, minuto, segundo):
    if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
        if hora == 0:
            horaConvertida = 12
            return ("%d:%02d:%02d pm" % (horaConvertida, minuto, segundo))
        if 1 <= hora <= 12:
            return ("%d:%02d:%02d am" % (hora, minuto, segundo))
        if 13 <= hora <= 23:
            horaConvertida = hora - 12
            return ("%d:%02d:%02d pm" % (horaConvertida, minuto, segundo))

    return "Error"


#Programa principal
def main():
    hora = int(input("Teclee la hora del tiempo actual: "))
    minuto = int(input("Teclee el minuto del tiempo actual: "))
    segundo= int(input("Teclee el segundo del tiempo actual: "))

    tiempoActual = convertirTiempo(hora, minuto, segundo)

    print("")
    print(tiempoActual)


#Corre el programa principal
main()
