#Autor: Saúl Figueroa Conde
#Matrícula: A01747306
#Grupo: 02
#Este programa lee las horas, minutos y segundos dados por el usuario y luego imprime la hora en formato de 12 hrs.
#-------------------------------------------------------------------------------------------------------------------


#Se declara la función calcularHora. Recibe como parámetros el valor de las horas, minutos y segundos dados por el
#usuario. Esta función incluye todas las condiciones para checar si la hora ingresada es valida y también tiene las
#instrucciones necesarias para convertir las horas del formato de 24 hrs al formato de 12 hrs. Al final, la función
#regresa el nuevo valor de horas, minutos y segundos.

am_pm = ""

def calcularHora(horas, minutos, segundos):

    if horas >= 0 and horas < 12:
        if minutos > 0 or minutos < 60 or segundos > 0 or segundos < 60:
            am_pm = "a.m."
            return horas, minutos, segundos, am_pm
        else:
            print("error")
            main()

    elif horas == 12:
            if minutos >= 0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
                am_pm = "p.m."
                return horas, minutos, segundos, am_pm
            else:
                print("error")
                main()

    elif horas >= 13 and horas <= 23:
        if minutos >= 0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
            am_pm = "p.m."
            horas = horas - 12
            return horas, minutos, segundos, am_pm
        else:
            print("error")
            main()

    elif horas == 24:
        if minutos >= 0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
            horas = 0
            am_pm = "a.m."
            return horas, minutos, segundos, am_pm
        else:
            print("error")
            main()

    elif horas < 0 or horas > 24:
        print("error")
        main()


#Se declara la función main. Aquí se le pregunat al usuario la cantidad de horas, minutos y segundos que quiere
#convertir al formato de 12 hrs. y estos valores se envían a la función calcularHora. Una vez que la función
#calcularHora regresa estos valores, la función main imprime el output correspondiente (que es la hora ingresada
#por el usuario en formato de 12 hrs).

def main():
    horas = int(input("Teclee el número de horas por favor: "))
    minutos = int(input("Teclee el número de minutos por favor: "))
    segundos = int(input("Teclee el número de segundos por favor: "))

    time12 = calcularHora(horas, minutos, segundos)

    print("")
    print("La hora que indicó es: {}:{}:{} {} en el formato de 12 hrs.".format(time12[0], time12[1], time12[2], time12[3]))
    salir = input("Muchas gracias por haber usado este programa.")
    quit()

#Se llama a la función main. Así corre cada una de las funciones desempeñando la tarea designada para dar solución
#a la problemática planteada.
main()