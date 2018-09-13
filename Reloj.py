#Autor: Alan Diaz Carrera
#Calcular la hora en un formato de 12 horas aun si la hora que se tiene es en formato de 24

def horas(hora):
    if hora >=12 and hora>=23:
        hora = hora-12
        return hora
    if hora==0 or hora== 00:
        hora = 12
        return hora

def tiempo(hora, minuto, segundo):
    print("La hora es: ",(hora, minuto, segundo))
def main():
    hora = int(input("hora: "))
    minuto= int(input("minutos: "))
    segundo = int(input("segundo: "))
    if hora <=00 and hora<=23 and minuto<=59 and minuto >=00 and segundo >=00 and segundo<=59:
        horas(hora)
        tiempo(hora, minuto, segundo)
    else:
        print("Error")
main()