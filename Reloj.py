#Arturo Márquez Olivar. A01376086.
#Recibe la hora en formato 24 horas y la transforma a formato 12 horas.


#Convierte número por número a las horas recibidas en el main.
def convertidorDeHora(horas, minutos, segundos):
    if horas == 0:
        horas = 12
        return horas
    else:
        if horas == 13:
            horas = 1
            return horas
        else:
            if horas == 14:
                horas = 2
                return horas
            else:
                if horas == 15:
                    horas = 3
                    return horas
                else:
                    if horas == 16:
                        horas = 4
                        return horas
                    else:
                        if horas == 17:
                            horas = 5
                            return horas
                        else:
                            if horas == 18:
                                horas = 6
                                return horas
                            else:
                                if horas == 19:
                                    horas = 7
                                    return horas
                                else:
                                    if horas == 20:
                                        horas = 8
                                        return horas
                                    else:
                                        if horas == 21:
                                            horas = 9
                                            return horas
                                        else:
                                            if horas == 22:
                                                horas = 10
                                                return horas
                                            else:
                                                if horas == 23:
                                                    horas = 11
                                                    return horas
                                                else:
                                                    horas = horas
                                                    return horas


#Recibe los datos de horas, minutos y segundos y decide si puede llamar a la funcion que convierte o manda error.
def main():
    horas = int(input("¿Cuáles son las horas en formato 24 horas?"))
    minutos = int(input("¿Cuáles son los minutos?"))
    segundos = int(input("¿Con cuántos segundos?"))

    hora = convertidorDeHora(horas, minutos, segundos)
    if horas >= 0 and horas <= 24 and minutos >= 0 and minutos <= 60 and segundos >= 0 and segundos <= 60:
        print("""La hora en formato de 12 horas es: 
        %.2d:%.2d:%.2d.""" % (hora, minutos, segundos))
    else:
        print("Error")


#Llamada a la función main.
main()