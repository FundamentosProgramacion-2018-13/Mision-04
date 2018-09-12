#Mariana Caballero Cabrera  A01376544
# Programa que convierte la hora en formato de 12 hrs


# Recibe la hora y la cambia a formato de 12 hrs

def calcularHora (hora):

    if hora >=0 and hora<=12:
        horaFormato = hora

    elif hora>=13 and hora <=24:
        horaFormato = hora - 12

    return horaFormato


# Función principal

def main ():

    hora = int(input("Hora: "))
    minuto = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    if hora >=0 and hora <=24 and minuto<60 and segundos<60:
        horaFormato = calcularHora(hora)
        print ("Hora: %d:%02d:%02d hrs" % (horaFormato,minuto,segundos))

    else:
        print ("Error")

#Llamamos a la función principal

main()

