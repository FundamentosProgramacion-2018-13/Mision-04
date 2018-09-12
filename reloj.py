#Rodolfo Anibal Altamirano Sánchez, A01377949
#Se te da la hora en un formato de 24 horas con minutos y segundos y la debes convertir en un formato de 12 horas. Si te da un horario ilógico, imprime error

#Hace la conversion a formato de 12 horas
def convertirFormato12Horas(hora):
    if hora == 0:
        return 12
    if hora <= 12:
        return hora
    if hora > 12:
        return hora%12

#Hace el calculo a pm o am dependiendo de la hora
def sacarPmAm(hora):
    if hora >= 12:
        return "pm"
    return "am"

#Se llaman las dos funciones y las imprime en forma de reloj de 12 horas o imprime error si no existe
def main():
    #Se escriben las variables y se les da valor
    hora = int(input("Teclea la hora: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    horaConvertida = convertirFormato12Horas(hora)
    pmAm = sacarPmAm(hora)
    #Si el horario es ilogico, simplemente imprime error
    if hora < 0 or hora > 23 or segundos > 59 or segundos < 0 or minutos > 59 or minutos < 0:
        print ("Error")

    #si es logico imprime el reloj
    else:
        print (horaConvertida,":",minutos,":",segundos ,pmAm)

main()