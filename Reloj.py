# Autor: Humberto Carrillo Gómez
# Descripción: Este programa convierte las horas en formato de 24 horas a formato de 12 horas

# Convierte las horas en formato de 24 horas a formato de 12.
def calcularFormatoDoce(hora):

    if hora == 0:
        hora = 12
    if hora <= 12:
        hora = hora
    if hora >= 13 and hora<=23:
        hora = hora-12

    return hora


# Función principal: resuelve el problema.
def main():
    hora= int(input("Teclea la hora: "))
    minuto= int(input("Teclea el minuto: "))
    segundo= int(input("Teclea el segundo: "))
    formatoDoce= calcularFormatoDoce(hora)

    if hora >= 24 or hora < 0 or minuto >= 60 or minuto < 0 or segundo >= 60 or segundo < 0:
        print("Error")
    elif hora == 0 and hora <= 11 :
        print("La hora en formato de doce horas es: %d:%02d:%02d AM" % (formatoDoce, minuto, segundo))
    elif hora >=12 and hora <=23:
        print("La hora en formato de doce horas es: %d:%02d:%02d PM" % (formatoDoce, minuto, segundo))


#Llamado a la función principal
main()