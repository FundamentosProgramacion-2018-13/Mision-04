#Joshua Sánchez Martínez A01274269
#Convierte la hora de formato 24 a formato 12


#Covierte la hora a formato 12
def calcularHora(hora):


    if hora == 0:
        hora12 = 12
    else:
        if hora >= 1 and hora <= 11:
            hora12 = hora
        else:
            if hora == 12:
                hora12 = 12
            else:
                hora12 = hora - 12

    return hora12


#Función principal
def main ():
    horaFormato24 = int(input("Teclea la hora en formato 24 horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))


    if horaFormato24 >= 0 and horaFormato24 <=11 and minutos >=0 and minutos <=59 and segundos >=0 and segundos<=59:
        horaFormato12 = calcularHora(horaFormato24)

        print("La hora en formato 12 es: %d:%02d:%02d" % (horaFormato12,minutos,segundos), "AM")
    else:
        if horaFormato24 >= 12 and horaFormato24 <= 23 and minutos >= 0 and minutos <= 59 and segundos >= 0 and segundos <= 59:
            horaFormato12 = calcularHora(horaFormato24)

            print("La hora en formato 12 es: %d:%02d:%02d" % (horaFormato12, minutos, segundos), "PM")
        else:
            print("Error, no puedo calcular")


#Llamar a la función main
main()
