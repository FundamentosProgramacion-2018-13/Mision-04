#Damián Iván García Ravelo      A01376354
#Programa que convierte la hora en formato de 24 horas a 12 horas

def cambiarFormatoMatutino(horas): #Asigna las horas que contendrán "AM"
    if horas == 0:
        return 0
    if horas == 1:
        return 1
    if horas == 2:
        return 2
    if horas == 3:
        return 3
    if horas == 4:
        return 4
    if horas == 5:
        return 5
    if horas == 6:
        return 6
    if horas == 7:
        return 7
    if horas == 8:
        return 8
    if horas == 9:
        return 9
    if horas == 10:
        return 10
    if horas == 11:
        return 11

def cambiarHorasVespertino(horas): #Asigna las horas que contendrán "PM"
    if horas == 12:
        return 12
    if horas == 13:
        return 1
    if horas == 14:
        return 2
    if horas == 15:
        return 3
    if horas == 16:
        return 4
    if horas == 17:
        return 5
    if horas == 18:
        return 6
    if horas == 19:
        return 7
    if horas == 20:
        return 8
    if horas == 21:
        return 9
    if horas == 22:
        return 10
    if horas == 23:
        return 11

def main():
#Pregunta al usuario los valores del tiempo
    horas = int(input("Teclea las horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

#Asigna las dos funciones a dos variables distintas
    matutino = cambiarFormatoMatutino(horas)
    vespertino = cambiarHorasVespertino(horas)

#Delimita el tiempo posible y lo que no encaje le marca error
    if horas < 0 or horas > 23 or minutos < 0 or minutos > 60 or segundos < 0 or segundos >= 61 :
        print("Introduzca hora válida")
    elif horas >= 0 and horas <= 11:
        print("La hora en formato de 12 horas es: %d:%02d:%02d AM" % (matutino, minutos, segundos))
    elif horas >= 12 and horas <=23:
        print("La hora en formato de 12 horas es: %d:%02d:%02d PM" % (vespertino, minutos, segundos))

main()