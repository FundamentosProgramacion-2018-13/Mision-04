# Autor: Danhel Alejandro Mercado Velasco
# Sacar la hora en segundos

def calcularhora(horas, minutos, segundos):
    if (0 <= horas <= 23) and (0 <= minutos <= 59) and (0 <= segundos <= 59):
        if horas > 12:
            horas = horas - 12
        return ("Hora: %d:%02d:%02d pm" % (horas, minutos, segundos))
        return ("Hora: %d:%02d:%02d am" % (horas, minutos, segundos))
    else:
        return "error"

# Esta funcion lee los datos e imprime el resultado

def main():
    horas = int(input("Dame las horas por favor: "))
    minutos = int(input("Dame los minutos por favor: "))
    segundos = int(input("Dame los segundos por favor: "))
    calcularhora(horas, minutos, segundos)
    print(calcularhora(horas, minutos, segundos))

# Llama a la funcion main
main()