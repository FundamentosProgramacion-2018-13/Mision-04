# Autor: Oscar Macias Rodríguez
# Descripción: Convierte el formato de 24 horas al formato de 12 horas.

# Cambia el formato de las horas de 24 a 12 hrs.
def convertirFormato(horas):
    formato = int(0)
    if horas == 0:
        formato = horas + 12
        return formato
    if horas > 12:
        formato = horas - 12
        return formato
    return horas


# Indica si la hora ES AM o si es PM
def verificarAMPM(horas):
    if horas > 12:
        return "pm"
    return "am"


# Imprime la hora (hora, minutos, segundos)
def main():
    horas = int(input("Escribe la hora: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))


   formatoAMpM = verificarAMPM(horas)
   formato = convertirFormato(horas)

   if horas < 0 or minutos < 0 or segundos < 0:
    print("error")
   if horas > 23 or minutos > 59 or segundos >59:
    print("error")
   else: print("La hora es: %d:%02d:%02d" % (formato, minutos, segundos), formatoAMpM)


main()