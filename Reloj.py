#Autor Zabdiel Valentin.
#Conversión del formato 24 horas al 12 horas de la forma 0:00:00 AM/PM, si no se introduce un valor correcto marca error.


def conversionHora(a,b,c):
    if 13>a>=1 and 61>b>=0 and 61>c>=0:
        return ("Hora: %d:%02d:%02d AM" % (a,b,c))

    if 24>a>12 and 61>b>=0 and 61>c>=0:
        a=a-12
        return ("Hora: %d:%02d:%02d PM" % (a,b,c))

    if a==0 and 61>b>=0 and 61>c>=0:
        a=12
        return ("Hora: %d:%02d:%02d AM" % (a,b,c))

    else: #a<0 or a>23 or 0>b>60 or 0>c>60:
        return ("error")



def main():
    hora=int(input("Introdusca la hora: "))
    minuto=int(input("Introdusca los minutos: "))
    segundo=int(input("Introdusca los segundos: "))
    formato12=conversionHora(hora,minuto,segundo)
    print(formato12)



main()

