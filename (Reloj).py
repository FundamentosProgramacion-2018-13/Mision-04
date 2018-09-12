# Luis Jonathan Rosas Ramos
# A01377942

# Transforar un formato de 24 horas de un reloj a 12 horas

# transformar el formato de 24 horas a 12
def calcularHoras(x,m,s):
    # si el numero de horas esta entre 12 y 0 entonces sera la hora nomral, simpere y cuando los minutos
    # y segundos sean menores a 60
    if x <= 12 and x > 0 and m<=60 and s<=60:
        return ("Hora: %d:%02d:%02d" % (x, m, s))
    # si supera el numero 13, pero esta antes del 23 habra que restarle 12 al numero
    elif x >= 13 and x <=23 and m<=60 and s<=60:
        x = x-12
        return ("Hora: %d:%02d:%02d" % (x, m, s))
    # finalemtne si la hora es igual a 24 entonces el reloj se reinicia
    elif x == 24 and m<=60 and s<=60:
        x = 0
        return ("Hora: %d:%02d:%02d" % (x, m, s))
    # en el caso de que ningna de estas se cumplan marcara error
    else:
        return("Error")


# dfinir funcion principal
def main():
    h = int(input("¿Cuantas horas van de 0-24?: "))
    m = int(input("¿Cuantos minutos van?: "))
    s = int(input("¿Cuantos segundos van?: "))
    horaNueva = calcularHoras(h,m,s)
    print(horaNueva)

#Llamar funcion principal
main()