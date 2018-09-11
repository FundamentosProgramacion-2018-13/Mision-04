#Autor: Claudio Mayoral García
#Recibe la hora en formato de 24 hrs y lo cambia a formato de 12hrs pero si es una hora falsa manda un mensaje de error


#Cambia el formato de las horas de 24hrs a 12hrs con una función y regresa el resultado
def cambiarFormatoHora(hora):
    formato12hrs = 0
    if hora == 0:
        formato12hrs = hora + 12
        return formato12hrs
    if hora > 12:
        formato12hrs = hora - 12
        return formato12hrs
    return hora


#Añade el formato "am" y "pm" al formato de las horas y regresa el formato indicado(am o pm)
def esAmPm(hora):
    if hora > 12:
        return "pm"
    return "am"


#Función principal pide los valores hora, minuto, segundo e imprime la hora 
#pero si no cumple con los requisitos imprime "error"
def main():
    hora = int(input("Escribe la hora: "))
    minuto = int(input("Escribe el minuto: "))
    segundo = int(input("Escribe el segundo: "))
    formatoAmPm = esAmPm(hora)
    formato12hrs = cambiarFormatoHora(hora)
    if hora < 0 or minuto < 0 or segundo < 0:
        print("error")
    elif hora > 23 or minuto > 59 or segundo > 59:
        print("error")
    else:
        print("La hora es: %d:%02d:%02d" % (formato12hrs, minuto, segundo), formatoAmPm)


#Llama a la función Principal
main()
