#Autor: David Rodriguez
#Cambia el formato de 24 horas a 12 horas


#Determina si los valores son válidos y cambia el formato a 12 horas restando 12 a las horas si estas son mayores a 12
def cambiarFormato(horas24, minutos, segundos):
    if horas24 < 25 and minutos < 61 and segundos < 61:
        if horas24 > 12:
            horas = (horas24-12)
        else:
            horas = horas24
    else:
        horas = "Error"
    return horas


#Función principal
def main():
    horas24 = int(input("Dame las horas: "))
    minutos = int(input("Dame los minutos: "))
    segundos = int(input("Dame los segundos: "))
    horas = cambiarFormato(horas24, minutos, segundos)
    if horas ==horas24:
        print("La hora es: ", horas, ":", minutos, ":", segundos, "AM")
    elif horas == "Error":
        print("Error")
    else:
        print("La hora es: ", horas, ":", minutos, ":", segundos, "PM")


main()

