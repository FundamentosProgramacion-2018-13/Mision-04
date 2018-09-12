#Autor: Zoe Caballero Dominguez
#Este programa recibe la hora en formato de 24 horas y la devuelve en formato de 12 horas

#Convierte la hora en formato de 24 horas a formato de 12 horas
def convertirHora(hora, minutos, segundos):
    if hora>=1 and hora <= 12:
        return "La hora es: %02d:%02d:%02d" % (hora, minutos, segundos)
    elif hora > 12 and hora < 23:
        hora = hora - 12
        return "La hora es: %02d:%02d:%02d" % (hora, minutos, segundos)
    elif hora == 0:
        hora = 12
        return "La hora es: %02d:%02d:%02d" % (hora, minutos, segundos)
    else:
        return "Error. Vuelva a ingresar los datos."


#Función principal
def main():
    hora = int(input("Escribe la hora en formato de 24 horas: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))

    print(convertirHora(hora, minutos, segundos))


#Llamar a la función
main()