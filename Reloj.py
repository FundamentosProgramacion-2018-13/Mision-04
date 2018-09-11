# Author: Ivan Honc Ayón     A01376466       Grupo 02
# Descripción: Este programa convierte la hora de formato 24hrs. a formato 12hrs.


# Esta función recibe las horas, los minutos y los segundos y los convierte a formato 12hrs,
# regresa una cadena con el horario convertido o con un mensaje de error.
def calcularHoraFormatoDoceHoras(hora, minutos, segundos):
    if hora>=0 and hora<=11 and minutos>=0 and minutos<60 and segundos>=0 and segundos<60:
        if hora==0:
            horaDoce = 12
        if hora>0 and hora<=11:
            horaDoce = hora
        horaFormatoDoceHoras = str(horaDoce)+":"+str(minutos)+":"+str(segundos)+" am"
    if hora>=12 and hora<=23 and minutos>=0 and minutos<60 and segundos>=0 and segundos<60:
        if hora==12:
            horaDoce = 12
        if hora>12 and hora<=23:
            horaDoce = hora-12
        horaFormatoDoceHoras = str(horaDoce)+":"+str(minutos)+":"+str(segundos)+" pm"
    if hora<0 or hora>23 or minutos<0 or minutos>=60 or segundos<0 or segundos>=60:
        horaFormatoDoceHoras = "Error: Se introdujeron datos inválidos."

    return horaFormatoDoceHoras


# Esta es la función principal que recibe los valores del usuario, manda a llamar a las otras funciones,
# e imprime la hora en formato 12hrs.
def main():
    hora = int(input("Escribe la hora (sin minutos ni segundos) en formato de 24hrs: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))
    horaFormatoDoceHoras = calcularHoraFormatoDoceHoras(hora, minutos, segundos)
    
    print(horaFormatoDoceHoras)


main()
