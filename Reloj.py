#Irma Gómez Carmona, A01747743
#Convertir la hora en formato 24 horas, tomando en cuenta horas, minutos y segundos

def convertirHora(hora): #Si las horas son mayores a 12 se le resta 12 para obtenerla en formato 12 horas, pero si es menor o igual a 12 se queda igual
    if hora==0:
        hora12=12
    elif hora>0 and hora<=12:
        hora12=hora
    elif hora>12 and hora <=24:
        hora12=hora-12
    return hora12

def main ():  #Obtener valores, llamar a las otras funciones y mostrar resultados
    print("---Hora en formato 24 hrs---")
    hora = int(input("Horas:"))
    minutos = int(input("Minutos:"))
    segundos = int(input("Segundos:"))

    if hora>=0 and hora <=24 and minutos>=0 and minutos<=60 and segundos>=0 and segundos<=60:

        formato12=convertirHora(hora)

        print("---Hora en formato 12 hrs---")
        print("%02d:%02d:%02d"%(formato12,minutos,segundos))
    else:
        print("--Hora inválida--")


main ()
