#Emiliano Heredia A01377072
#Cambia del formato de 24hrs a 12 hrs.
def main():
    flag = True
    while(flag):
        hora = int(input("Ingrese la hora: "))
        minuto = int(input("Ingrese el minuto: "))
        segundo = int(input("ingrese el segundo: "))
        nhora, ampm, err = calcularHora(hora)
        err = checarMS(minuto, segundo)

        if(err):
            print("Valores numericos fuera del rango permitido. Favor de ingresar numeros validos")
        else:
            print("La hora en formato de 12 hrs. es la siguiente: %02d:%02d:%02d %s"%(nhora,minuto,segundo,ampm))
            flag = False


#Checa que los minutos y segundos esten dentro de los valores validos
def checarMS(min, seg):
    if(min<0 or min>59 or seg<0 or seg > 59):
        return True
    else:
        return False


#Checa que la hora este dentro de los valores valido y cambia del formato de 24hrs al de 12hrs. 
def calcularHora(hora):
    if(0<hora<13):
        return hora, "am", False
    elif(hora==0):
        return hora, "pm", False
    elif(hora<24):
        return hora-12, "pm", False
    else:
        return 0, "", True


main()