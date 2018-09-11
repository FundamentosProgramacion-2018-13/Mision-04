#Autor: Alejandro Torices Oliva
#Es un programa que convierte la hora del formato 24hrs a formato 12 hrs

#Función que checa la validez de la hora y regresa la equivalencia en formato 12 horas.
def checarHora(hora):
    if hora >= 0 and hora <24:
        if hora > 0 and hora <=12:
            return hora
        else:
            if hora == 0:
                return 12
            elif hora == 13:
                return 1
            elif hora == 14:
                return 2
            elif hora == 15:
                return 3
            elif hora == 16:
                return 4
            elif hora == 17:
                return 5
            elif hora == 18:
                return 6
            elif hora == 19:
                return 7
            elif hora == 20:
                return 8
            elif hora == 21:
                return 9
            elif hora == 22:
                return 10
            else:
                return 11
    else:
        return 666                    #el valor cumple la función de "False", aún no sé como usarlo correctamente


#Función que checa la valiez de los minutos
def checarMinutos(minutos):
    if minutos >=0 and minutos <60:
        return minutos
    else:
        return 666


#Función que checa la validez de los segundos.
def checarSegundos(segundos):
    if segundos >=0 and segundos <60:
        return segundos
    else:
        return 666


#Función principal.
def main():
    hora = int(input("Hora: "))
    minuto = int(input("Minutos: "))
    segundo = int(input("Segundos: "))

    horas = checarHora(hora)
    minutos = checarMinutos(minuto)
    segundos = checarSegundos(segundo)

    print(" ")
    if horas != 666 and minutos != 666 and segundos != 666:
        print("%02d:%02d:%02d" % (horas, minutos, segundos))
    else:
        print("Error")


main()