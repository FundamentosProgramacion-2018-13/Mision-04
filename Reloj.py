# Autor: Luis Humberto Burgueño Paz
# Convierte la hora en formato de 24 horas al formato de 12 horas


#Pasa de formato en 24 horas a formato en 12 horas
def pasarDe24a12(horas24):
    if horas24 < 13 and horas24 != 0:
        return horas24
    else:
        if horas24 == 0:
            return 12
        else:
            horas12 = horas24 - 12
            return horas12


# Define si se debe imprimir a.m. o p.m.
def calcularAMoPM(horas24):
    if horas24 < 13:
        return "a.m."
    else:
        return "p.m."


#Función Principal: Lee la hora en formato de 24 horas y llama a las demás funciones para imprimirla en formato de 12 horas
def main():
    horas24 = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    if horas24 < 0 or horas24 > 23:
        print("error")
    else:
        if minutos < 0 or minutos > 59:
            print("error")
        if segundos < 0 or segundos > 59:
            print("error")
        else:
            horas12 = pasarDe24a12(horas24)
            amOpm = calcularAMoPM(horas24)
            print("Son las %02d:%02d:%02d %s" % (horas12, minutos, segundos, amOpm))




main()