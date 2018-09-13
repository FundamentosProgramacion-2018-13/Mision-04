#Autor: Michelle Sánchez Guerrero
#Descripción: Programa que convierte la hora en formato 24 horas al formato 12 horas.


#Función que convierte las horas del formato 24 horas, al formato 12 horas.
def convertirFormatoHora(hora):

    if hora >= 13 and hora <=23:
        hora = hora - 12
    elif hora == 0:
        hora = 12

    return hora


#Formato que determina si la hora es am o pm.
def calcularAmPm(hora):

    formato = "am"

    if hora >= 12 and hora <= 23:
        formato = "pm"

    return formato


#Función principal. Lee datos e imprime resultados.
def main():
    hora = int(input("Hora: "))
    minuto = int(input("Minutos: "))
    segundo = int(input("Segundos: "))

    print()
    if hora >=0 and hora <= 23 and minuto >=0 and minuto <=59 and segundo >=0 and segundo <=59:
        formatoHora = convertirFormatoHora(hora)
        formatoAmPm = calcularAmPm(hora)
        print("La hora es: %d:%02d:%02d %s" % (formatoHora, minuto, segundo, formatoAmPm))
    else:
        print("Error")


#Llamar a la función principal.
main()