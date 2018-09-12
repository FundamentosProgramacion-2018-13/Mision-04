#Francisco Ariel Arenas Enciso
#Programa para pasar horas en formato de 24hr a 12hr


'''
Esta función recibe los valores para la hor, los minutos y los segundos de la función "main()". Mediante operadores
lógicos y relacionales compara los valores recibidos para determinar que hora, minutos y segudnos debera regrsar
a "main()"
'''
def calcularHora(horas, minutos, segundos):
    if horas == 00 and minutos >= 00 and minutos <= 59 and segundos >= 00 and segundos <= 59:
        horas = 12
        nuevoFormato = str(horas) + ":" + ":" + str(minutos) + ":" + str(segundos) + "AM"
    elif horas > 00 and horas < 11 and minutos >= 00 and minutos <= 59 and segundos >= 00 and segundos <= 59:
        horas = horas
        nuevoFormato = str(horas) + ":" + str(minutos) + ":" + str(segundos) + "AM"
    elif horas == 12 and minutos >= 00 and minutos <= 59 and segundos >= 00 and segundos <= 59:
        horas = 12
        nuevoFormato = str(horas) + ":" + ":" + str(minutos) + ":" + str(segundos) + "PM"
    elif horas > 12 and horas <= 23 and minutos >= 00 and minutos <= 59 and segundos >= 00 and segundos <= 59:
        horas = (horas - 12)
        nuevoFormato= str(horas) + ":" + str(minutos) + ":" + str(segundos) + "PM"
    elif horas < 00 or horas >= 24 or minutos < 00 or minutos >= 60 or segundos < 00 or segundos >= 60:
        nuevoFormato = "Estos datos no son válidos"
    return nuevoFormato


'''
Función main, la cual controla todo el programa, envía los valores dados por el usuario a la función "calcularHora()"
recibe los datos de ésta última e imprime el formato convertido a 12 hrs i es correcta la hora dada. En caso de 
no serlo, regresa un mensajer de error. 
'''
def main():
    horas = int(input("Por favor introduzca solo la hora en un formato de 24hrs: "))
    minutos = int(input("Por favor introduzca la cantidad de minutos: "))
    segundos = int(input("Por favor introduzca la cantidad de segundos: "))
    hora_en_formato_doce = calcularHora(horas, minutos, segundos)
    print("------------------------------------")
    print("La hora es: ", (hora_en_formato_doce))


main()