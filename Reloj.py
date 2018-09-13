#Autor: Samantha Martínez Franco A01747686
#Pasar la hora de formato 24 horas a 12 horas


#función que pasa de 24 a 12 horas
def calcularHora (hora,minuto,segundo):
    if hora==0:     #la hora 0 es la hora 12 am
        hora=12
    if hora>12:
        tiempo=hora-12
        return tiempo
    return hora


#función principal
def  main():
    horas=int(input("Hora: "))       #pedir valores
    if (horas < 0 or horas>23):           #valores mayores a 23 o negativos marcan error
        print("ERROR ")
    else:
        minutos=int(input("Minutos: "))      #si pones negativos o mas de 59 minutos
        if minutos<0 or minutos>59:
            print("ERROR")
        else:
            segundos=int(input("Segundos: "))    #si pones negativos o mas de 59 segundos
            if segundos<0 or segundos>59:
                print("ERROR")
            elif horas >= 12:
                horas12 = calcularHora(horas, minutos, segundos)  # si las horas son de la tarde
                print("La hora es: %d:%02d:%02d" % (horas12, minutos, segundos), "p.m")
            else:
                horas12 = calcularHora(horas, minutos, segundos)
                print("La hora es: %d:%02d:%02d" % (horas12, minutos, segundos), "a.m")  # si son de ma mañana


main()