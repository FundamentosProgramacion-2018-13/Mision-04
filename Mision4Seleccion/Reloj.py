# Autor: Roberto Emmanuel González Muñoz
# Escribe un programa que convierta la hora en formato de 24 horas al formato de 12 hrs.

# Calcula y define la hora dada.
def calcularHora(horas, minutos, segundos):
    if 13 <= horas <= 23:
        hora = (horas - 12), minutos, segundos
        return hora

    elif 1 <= horas <= 12:
        hora = horas, minutos, segundos
        return hora

    elif horas == 0:
        hora = (horas + 12), minutos, segundos
        return hora


def main():

    # Recibimos los datos del usuario
    horas = int(input("Teclea las horas: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    # Establecemos un filtro para los numeros introducidos por el usuario.
    if (0 <= horas <= 23) & (0 <= minutos <= 59) & (0 <= segundos <= 59):
        hora = calcularHora(horas, minutos, segundos)
        print("Son las %d horas con %d minutos y %d segundos" % hora)
        print("%0d:%0d:%0d" % hora)
    else:
        print("ERROR")


main()