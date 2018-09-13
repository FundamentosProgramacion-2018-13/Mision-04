# David Isaí López Jaimes            A01748363
#  Convierte la hora de formato 24hrs a 12hrs


def formatoDoce(h, m, s): # Asigna los minutos y segundo normales, ya que estos no afectan, para la hora calcula si es mayor a
    hora = h   #  12 por que este es el limite y si es mayor lo convierte en formato 12hrs
    if h > 12:
        hora = h - 12
    if h == 0 and m == 0 and s == 0:
        hora = h + 12
        m = 0
        s = 0
    return hora, m, s


def main():            # Aquí leemos y calculamos la funcion anterior e imprimimos resultados
    horas = int(input("Teclea la hora en formato 24hrs: "))
    minutos = int(input("Teclea los minutos en formato 24hrs: "))
    segundos = int(input("Teclea los segundos en formato 24hrs: "))

    if horas > 24 or minutos > 59 or segundos > 59:
        print("Error")
    else:
        horaDoce = formatoDoce(horas, minutos, segundos)
        print("Hora en formato 12hrs: %d:%02d:%02d hrs" % (horaDoce))

main()