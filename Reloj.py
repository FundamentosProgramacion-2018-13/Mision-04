# Autor: Luis Armando Miranda Alcocer
# Descripción: Convertir la hora de un formato de 24 horas a uno de 12 horas.

def calcularHorasFormatoDoce (horasFormatoVeinticuatro): #Clasifica las horas, si se teclea 13, se regresa 1, y así sucesivamente.
    if horasFormatoVeinticuatro == 13:
        horasFormatoDoce = 1
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 14:
        horasFormatoDoce = 2
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 15:
        horasFormatoDoce = 3
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 16:
        horasFormatoDoce = 4
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 17:
        horasFormatoDoce = 5
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 18:
        horasFormatoDoce = 6
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 19:
        horasFormatoDoce = 7
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 20:
        horasFormatoDoce = 8
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 21:
        horasFormatoDoce = 9
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 22:
        horasFormatoDoce = 10
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 23:
        horasFormatoDoce = 11
        return horasFormatoDoce

    if horasFormatoVeinticuatro == 00: #Si se teclea 0 en formato 24 horas, en formato 12 serán las 12
        horasFormatoDoce = "12"
        return horasFormatoDoce



def main ():
    horasFormatoVeinticuatro= int(input("Ingresa las horas en formato 24 horas: ")) #Se leen los datos de entrada
    minutos= int(input("Ingresa los minutos en formato 24 horas: "))
    segundos= int(input("Ingresa los segundos en formato 24 horas: "))

#Se empieza por los errores, si no posee errores puede proceder a calcular la hora en formato 12 horas.
    if horasFormatoVeinticuatro > 23 or horasFormatoVeinticuatro < 0:
        print ("Error")

    if (minutos > 59 or minutos < 0) or (segundos >59 or segundos <0) :
        print ("Error")
    else: #Si no tiene errores, se calcula la hora.
        if horasFormatoVeinticuatro < 12 and horasFormatoVeinticuatro > 00: #Si la hora es entre la 1 y las 12, la hora es la misma en ambos formatos.
            print("Son las: ", horasFormatoVeinticuatro, ": %.2d" % minutos, ': %.2d' % segundos, "horas.")

        if horasFormatoVeinticuatro > 12 and horasFormatoVeinticuatro <= 23 or horasFormatoVeinticuatro == 0: #Si la hora es desde las 13 a las 00, se cambia la hora de formato.
            horasFormatoDoce = calcularHorasFormatoDoce(horasFormatoVeinticuatro) #Los segundos y minutos se mantienen igual
            print("Son las: ", horasFormatoDoce, ": %.2d" % minutos, ': %.2d' % segundos, "horas.")


main()