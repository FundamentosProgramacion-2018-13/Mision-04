#Autor Daniel Cordova Bermudez
#Grupo 02
#Descripcion: El programa se intorduce las horas, minutos y segundos, se vereifica que sean correctos y se cambia el formato del horario.

#Funcion que verifica si los datos son correctos en el caso que no lo sea envia error, tambien convierte el horario PM o AM y regresa el resultado.

def formatoHorario(horas, minutos, segundos):
    if (0 <= horas <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):

        if horas > 12:
            horas = horas - 12
            return ("Hora: %d:%02d:%02d PM" % (horas, minutos, segundos))
        else:
            return ("Hora: %d:%02d:%02d AM" % (horas, minutos, segundos))

    else:
        return ("ERROR")

#Función que pide la información, ademas de imprimir el horario final.

def main ():

    horas = int(input("Escribe las Horas: "))
    minutos = int(input("Escribe los Minutos: "))
    segundos = int(input("Escribe los Segundos: "))

    print(formatoHorario(horas,minutos,segundos))

#Llama a la funcion main.
main()