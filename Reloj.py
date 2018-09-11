#Jesús Roberto Herrera Vieyra // A01377230

#Programa para convertir el formato de un reloj

#función para convertir la hora si es posible
def convertirHora(hora, minuto, segundo):
    if hora >= 0 and hora <= 23 and minuto >= 0 and minuto <= 59 and segundo >= 0 and segundo <= 59:
        horaNueva = hora - 12
        return horaNueva

    else:
        return "Hora inválida"


def main():
    hora= int(input("Teclee la hora: "))
    minuto= int(input("Teclee el minuto: "))
    segundo= int(input("Teclee el segundo: "))
    conversion = convertirHora(hora,minuto,segundo)

    if conversion != "Hora inválida":
        if hora>12:
            print("Son las %02d:%02d:%02d PM" %(conversion,minuto,segundo))

        else:
            print("Son las %02d:%02d:%02d AM" %(hora,minuto,segundo))

    else:
        print("HORA INVÁLIDA")

main()