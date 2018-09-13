# Autor: Carlos Alberto Reyes Ortiz
# Tranforma una hora dada en formato 24 hrs a formato 12 hrs



def cambiarFormatoVeintiCuatroHoras_a_FormatoDoceHoras(horaFormatoVeintiCuatroHoras): #Transforma la hora de formato
    #                                                                                  24 hrs a formato 12 hrs
    if horaFormatoVeintiCuatroHoras == 0:
        return 12
    elif horaFormatoVeintiCuatroHoras == 1:
        return 1
    elif horaFormatoVeintiCuatroHoras == 2:
        return 2
    elif horaFormatoVeintiCuatroHoras == 3:
        return 3
    elif horaFormatoVeintiCuatroHoras == 4:
        return 4
    elif horaFormatoVeintiCuatroHoras == 5:
        return 5
    elif horaFormatoVeintiCuatroHoras == 6:
        return 6
    elif horaFormatoVeintiCuatroHoras == 7:
        return 7
    elif horaFormatoVeintiCuatroHoras == 8:
        return 8
    elif horaFormatoVeintiCuatroHoras == 9:
        return 9
    elif horaFormatoVeintiCuatroHoras == 10:
        return 10
    elif horaFormatoVeintiCuatroHoras == 11:
        return 11
    elif horaFormatoVeintiCuatroHoras == 12:
        return 12
    elif horaFormatoVeintiCuatroHoras == 13:
        return 1
    elif horaFormatoVeintiCuatroHoras == 14:
        return 2
    elif horaFormatoVeintiCuatroHoras == 15:
        return 3
    elif horaFormatoVeintiCuatroHoras == 16:
        return 4
    elif horaFormatoVeintiCuatroHoras== 17:
        return 5
    elif horaFormatoVeintiCuatroHoras == 18:
        return 6
    elif horaFormatoVeintiCuatroHoras == 19:
        return 7
    elif horaFormatoVeintiCuatroHoras == 20:
        return 8
    elif horaFormatoVeintiCuatroHoras == 21:
        return 9
    elif horaFormatoVeintiCuatroHoras == 22:
        return 10
    elif horaFormatoVeintiCuatroHoras == 23:
        return 11




def main(): #Función principal: Te da la hora en formato de 12 hrs dada en formato de 24 hrs.
            #                   Si marcas una hora inválida te lo hace saber
    print("Escribe la hora en formato 24 horas")
    horaFormatoVeintiCuatroHoras = int(input("Hora: "))
    minuto = int(input("Minuto: "))
    segundo = int(input("Segundo: "))
    print()
    horaFormatoDoceHoras = cambiarFormatoVeintiCuatroHoras_a_FormatoDoceHoras(horaFormatoVeintiCuatroHoras)
    if minuto > 59 or minuto < 0 or segundo > 59 or segundo < 0:
        print(""" "ERROR" Favor de introducir una hora válida""""")
    elif horaFormatoVeintiCuatroHoras <= 11 and horaFormatoVeintiCuatroHoras >= 0:
        print("La hora en formato de 12 horas es: %d:%02d:%02d AM" % (horaFormatoDoceHoras, minuto, segundo))
    elif horaFormatoVeintiCuatroHoras >= 12 and horaFormatoVeintiCuatroHoras <= 23:
        print("La hora en formato de 12 horas es: %d:%02d:%02d PM" % (horaFormatoDoceHoras, minuto, segundo))
    else: print(""" "ERROR" Favor de introducir una hora válida""""")




#Llamar función
main()
