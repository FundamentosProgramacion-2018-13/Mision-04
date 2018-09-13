# Oscar Alejandro Torres Maya, A01377686
# El usuario introduce la hora en formato de 24hrs y el programa lo pasa a formato de 12hrs

# Función para convertir del formato de veinticuatro horas al de doce horas
def convertirFormato(veintiCuatroHoras):
    if veintiCuatroHoras == 0:
        return 12
    elif veintiCuatroHoras == 1:
        return 1
    elif veintiCuatroHoras == 2:
        return 2
    elif veintiCuatroHoras == 3:
        return 3
    elif veintiCuatroHoras == 4:
        return 4
    elif veintiCuatroHoras == 5:
        return 5
    elif veintiCuatroHoras == 6:
        return 6
    elif veintiCuatroHoras == 7:
        return 7
    elif veintiCuatroHoras == 8:
        return 8
    elif veintiCuatroHoras == 9:
        return 9
    elif veintiCuatroHoras == 10:
        return 10
    elif veintiCuatroHoras == 11:
        return 11
    elif veintiCuatroHoras == 12:
        return 12
    elif veintiCuatroHoras == 13:
        return 1
    elif veintiCuatroHoras == 14:
        return 2
    elif veintiCuatroHoras == 15:
        return 3
    elif veintiCuatroHoras == 16:
        return 4
    elif veintiCuatroHoras == 17:
        return 5
    elif veintiCuatroHoras == 18:
        return 6
    elif veintiCuatroHoras == 19:
        return 7
    elif veintiCuatroHoras == 20:
        return 8
    elif veintiCuatroHoras == 21:
        return 9
    elif veintiCuatroHoras == 22:
        return 10
    elif veintiCuatroHoras == 23:
        return 11


# Función principal
def main():
    print("Ingresa la hora en formato de 24 horas")
    horas = int(input("Cuál es la hora? "))
    minutos = int(input("Cuáles son los minutos? "))
    segundos = int(input("Cuáles son los segundos? "))
    veintiCuatroHoras = convertirFormato(horas)
    formatoDoceHoras = convertirFormato(veintiCuatroHoras)

    if horas < 0 or horas >=24 and minutos > 59 or minutos < 0 and segundos < 0 or segundos > 59:
        print("error")
    elif horas >= 0 and horas < 12:
        print ("La hora en el formato de 12 horas es: ", (formatoDoceHoras), ":", (minutos),":",(segundos), "a.m.")
    elif horas >= 12 and horas <= 23:
        print("La hora en el formato de 12 horas es: ", (formatoDoceHoras), ":", (minutos),":",(segundos), "p.m.")

# Llamada de función principal
main()