#Javier Alexandro Vargas Sánchez A01377718
#Programa que sirve para convertir la hora de un formato de 24 horas a uno de 12 horas


#Función que divide la hora entre 12 y obtiene el residuo de la división (la hora en formato de 12 horas)
def convertirFormato(hora):
    tiempoEn12 = hora % 12
    return tiempoEn12


#Función que define si la hora en formato de 12 horas es en la mañana o en la tarde
def calcularAmPm(hora):
    if hora <12:
        return  "A.M."
    if hora >= 12:
        return "P.M."


#Función principal con parámetros para facilitar la conversión
def main():
    hora = int(input("Teclea la hora en formato de 24 horas: "))
    minuto = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    if hora < 0 or hora > 24     or minuto < 0 or minuto >= 60    or segundos < 0 or segundos >= 60:
        print("Error")
    else:
        if hora != 0 and hora != 24:
            tiempoEn12 = convertirFormato(hora)
            amPm = calcularAmPm(hora)
            print("La hora en formato de 12 horas es: %d:%02d:%02d" % (tiempoEn12, minuto, segundos), amPm)

        else:
            hora = 12
            amPm = "A.M"
            print("La hora en formato de 12 horas es: %d:%02d:%02d" % (hora, minuto, segundos), amPm)


#Llamada a la función main
main()