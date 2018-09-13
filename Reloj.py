# Autor: Jonathan Sanabria Rocha
# Descripcion: Programa que convierta la hora en formato de 24 horas a formato de 12 horas.


# Convierte formato de 24 horas a 12 horas
def convertirFormato24A12Horas(hora,minuto,segundo):
    if hora > 12:
        formato12 = ("%.0f:%.0f:%.0f p.m." % (hora%12,minuto,segundo))
        return formato12
    elif hora == 12:
        formato12 = ("%.0f:%.0f:%.0f p.m." % (hora , minuto, segundo))
        return formato12
    else:
        formato12 = ("%.0f:%.0f:%.0f a.m." % (hora % 12, minuto, segundo))
        return formato12


# Funcion principal
def main():
    hora = int(input("Teclea la hora: "))
    minuto = int(input("Teclea el minuto: "))
    segundo = int(input("Teclea el segundo: "))
    if 0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59:
        horaActual = convertirFormato24A12Horas(hora,minuto,segundo)
        print(horaActual)
    else:
        horaInvalida = "Error"
        print (horaInvalida)


#Llama la funcion principal
main()