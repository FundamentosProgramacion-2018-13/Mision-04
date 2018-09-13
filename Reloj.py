#Autor: Luis Ricardo Chagala Cervantes.
#Convertir del formato 24 horas al 12 horas de la forma 0:00:00 AM/PM.


def conversionHora(hora, minutos, segundos):
    if 1 <= hora < 13 and 0 < minutos < 61 and 0 <= segundos < 61:
        return ("Hora: %d:%02d:%02d AM" % (hora, minutos, segundos))

    if 12 < hora < 24 and 0 <= minutos < 61 and 0 <= segundos < 61:
        hora = hora - 12
        return ("Hora: %d:%02d:%02d PM" % (hora, minutos, segundos))

    if hora == 0 and 0 < minutos <= 61 and 0 <= segundos < 61:
        hora = 12
        return ("Hora: %d:%02d:%02d AM" % (hora, minutos, segundos))

    else:
        return ("Error")


def imprimir(nuevoformato):
    print(nuevoformato)


def main():
    hora = int(input("Hora: "))
    minuto = int(input("Minutos: "))
    segundo = int(input("Segundos: "))
    nuevoformato = conversionHora(hora, minuto, segundo)
    imprimir(nuevoformato)



main()

