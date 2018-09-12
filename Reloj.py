# Alex Fernando Leyva Martinez - A01747078 - Grupo: 04
# Convierte una tiempo especifico en formato de 24 horas al de 12 horas

# Convierte la hora a formato de 12 dependiendo del valor
def convertirFormato(hora):
    if hora > 12:
        formato12 = (hora - 12)
        return formato12
    elif hora <= 12:
        formato12 = hora
        return formato12

# Dependiendo del valor, se define si es am o pm
def definirAmPm(hora):
    if hora < 12:
        horario = "am"
        return horario
    else:
        horario = "pm"
        return horario

# Analiza los datos dados, certificando si son válidos o no de acuerdo a las condiciones e imprime la cadena de la hora
def main():
    hora = int(input("Teclea la hora: "))
    minuto = int(input("Teclea el minuto: "))
    segundo = int(input("Teclea el segundo: "))
    formato12 = convertirFormato(hora)
    horario = definirAmPm(hora)
    if hora < 0 or minuto < 0 or segundo < 0:
        print("Error")
    if hora > 23 or minuto > 59 or segundo > 59:
        print("Error")
    else:
        print("Son las: %d:%02d:%02d " % (formato12, minuto, segundo),horario)

# Llama a la función principal
main()