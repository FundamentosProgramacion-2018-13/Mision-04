#Autor: Jose Luis Mata Lomeli
#Convertir la hora dada por el usuario en formato 24hrs a formato 12hrs

#Transformar la hora dada por el usuario a el otro formato

def tranformarHRS(hora24):

    if hora24 >= 0 and hora24 <= 12:

        hora_Igual = hora24
        return hora_Igual


    if hora24 >= 13 and hora24 <= 24:

        hora12 = hora24 - 12
        return hora12


def determinarAM(formato24):

    if formato24 >= 0 and formato24 <= 12:
        return("mañana (a.m)")

    if formato24 >= 13 and formato24 <= 23:
        return("tarde (p.m)")

def main():

    print("Escriba la hora en formato 24 horas")
    hora24 = int(input("Escriba la hora: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))

    hora12 = tranformarHRS(hora24)
    am_pm = determinarAM(hora24)

    print(" ")
    print(" ")

    print("hh/mm/ss en 24hrs seria: la(s) %02d hora(s) con %02d minuto(s) y %02d segundo(s) " % (hora24, minutos, segundos))
    print(" ")
    print("hh/mm/ss en 12hrs seria: las(s)%02d" %(hora12), "horas con %02d" %(minutos), "minuto(s) y %02d" %(segundos), "segundo(s) de la",(am_pm))
main()
