#encoding: UTF-8
#Autor: Alek Howland, A01747765
#Descripción: Convierte la hora en formato 24  a 12

#Convierte el tiempo de 24 a 12 usando selcción
def convertirTiempo(hora, minutos, segundos):
    if hora >= 0 and hora <= 24 and minutos >= 0 and minutos <= 59 and segundos >= 0 and segundos <= 59:
        if hora == 13:
            print("")
            print("1:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 14:
            print("")
            print("2:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 15:
            print("")
            print("3:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 16:
            print("")
            print("4:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 17:
            print("")
            print("5:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 18:
            print("")
            print("6:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 19:
            print("")
            print("7:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 20:
            print("")
            print("8:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 21:
            print("")
            print("9:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 22:
            print("")
            print("10:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 23:
            print("")
            print("11:%02d:%02d hrs" % (minutos, segundos))
        elif hora == 24:
            print("")
            print("0:%02d:%02d hrs" % (minutos, segundos))
        elif hora < 13:
            print("")
            print ("%d:%02d:%02d hrs" % (hora, minutos, segundos))
    else:
        print("")
        print ("error")

#Función principal
def main():

    hora = int(input("Introduce la hora en formato de 24: "))
    minutos = int(input("Introduce los minutos en formato de 24: "))
    segundos = int(input("Introduce los segundos en formato de 24: "))
    convertirTiempo(hora, minutos, segundos)

main()




