#Autor: Alberto Contreras Torres
#Convierte la hora en formato 24hrs a 12hrs

#Recibe la hora en formato 24hrs, Regrea la hora en formato 12 hrs
def calcularFormato12hrs (hora24):
    if hora24 == 1:
        return 1
    elif hora24 ==2:
        return 2
    elif hora24 ==3 :
        return 3
    elif hora24 ==4 :
        return 4
    elif hora24 ==5 :
        return 5
    elif hora24 ==6 :
        return 6
    elif hora24 ==7 :
        return 7
    elif hora24 ==8 :
        return 8
    elif hora24 ==9 :
        return 9
    elif hora24 ==10 :
        return 10
    elif hora24 == 11:
        return 11
    elif hora24 == 12:
        return 12
    elif hora24 == 13:
        return 1
    elif hora24 ==14 :
        return 2
    elif hora24 ==15 :
        return 3
    elif hora24 ==16 :
        return 4
    elif hora24 ==17 :
        return 5
    elif hora24 ==18 :
        return 6
    elif hora24 ==19 :
        return 7
    elif hora24 ==20 :
        return 8
    elif hora24 ==21 :
        return 9
    elif hora24 ==22 :
        return 10
    elif hora24 ==23:
        return 11
    else:
        print("ERROR")




#Funciòn principal
def main():
    hora24= int(input("Teclea la hora en formato 24hrs: "))
    minutos= int(input("Teclea los minutos: "))
    segundos= int(input("Teclea los segundos: "))
    hora12 = calcularFormato12hrs(hora24)
    if hora24 <= 0 and hora24 > 23 and minutos <= 0 and minutos >59 and segundos <=0 and segundos >59:
        print(("ERROR"))
    else:
        hora12 = calcularFormato12hrs(hora24)
        print("Hora: %d:%02d:%02d" % (hora12, minutos, segundos))

main()
