#Autor: David Alejandro Nicolás Palos
#Recibir una hora en el formato 24h y convertirlo a formato 12h



def convertirFormato(hora,minuto,segundo): #analiza dentro de que rango entra la hora dada y la divide para hacer la conversion de formato 24hrs a 12 hrs

        if hora == 0:
            hora12 = 12
            return hora12, minuto, segundo
        else:
            if hora > 12 and hora < 24:
                hora12 = hora - 12
                return hora12, minuto, segundo
            else:
                return hora, minuto, segundo

def imprimirHora(hora, minuto, segundo): #Se asegura de que los datos introducidos sean correspondientes al formato buscado, ordena
    if hora < 0 or hora > 23 or minuto < 0 or minuto > 59 or segundo < 0 or segundo > 59 :
        print("")
        print("error")
    else:
        if hora >= 0 and hora < 13:
            print("")
            print("Hora: %d:%02d:%02d AM" % convertirFormato(hora, minuto, segundo))
        if hora > 12 and hora < 24:
            print("")
            print("Hora: %d:%02d:%02d PM" % convertirFormato(hora, minuto, segundo))


def main(): #Funcion main, lee e imprime resultados
    hora = int(input("Escribe la hora sin minutos ni segundos: "))
    minuto = int(input("Escribe los minutos sin segundos: "))
    segundo = int(input("Escribe los segundos: "))
    imprimirHora(hora, minuto, segundo)


main()
