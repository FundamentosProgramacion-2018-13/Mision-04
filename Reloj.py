# encoding: UTF-8
# Autor: Diego Palmerin Bonada, A01747290
# Descripcion: Convierte la hora de formato 24h a 12h

pm = "pm"


# convierte el formato 24h a 12h si el formato es correcto
def conversorPrincipal(h,m,s):
    if (type(h) == int) and (0<=h<=24) and (type(m) == int) and (0<=h<=60) and (type(s) == int) and (0<=h<=60):
        if h >= 12:
            pm = "pm"
            h = h-12
        else:
            pm = "am"

        return "%02d:%02d:%02d %s" % (h, m, s, pm)
    else:
        print("Error")


#Obtiene variables e imprime resultados
def main():
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos= int(input("Segundos: "))

    print(conversorPrincipal(horas, minutos,segundos))


main()