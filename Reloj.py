"""
Nombre: Alexys Martín Coate Reyes
Martícula: A01746998
Descripción: Cambiar el formato de la hora (de 24hrs a 12hrs)

"""

#Verifica si la hora ingresada es correcta
def verificarHora(hora):
    if hora >= 0 and hora <= 12:
        return hora
    if hora > 12 and hora <=24:
        hora = hora-12
        return hora
    else:
        return "Error"


#Verifica si el minuto ingresado es correcto
def verificarMinuto(minutos):
    if minutos >= 0 and minutos < 60:
        return minutos
    else:
        return "Error"


#Verifica si los segundos ingresados son correctos
def verificarSegundos(segundos):
    if segundos >= 0 and segundos < 60:
        return segundos
    else:
        return "Error"


#Imprime todos las horas en formato de 24hrs y en 12hrs
def imprimir(hora, minutos, segundos):
    print("Formato de 24hrs: {:02}:{:02}:{:02}" .format(hora, verificarMinuto(minutos), verificarSegundos(segundos)))
    print("Formato de 12hrs: {:02}:{:02}:{:02}" .format(verificarHora(hora), verificarMinuto(minutos), verificarSegundos(segundos)))


#Verifica si la hora en general es correcta
def verificar(hora, minutos, segundos):
    if verificarHora(hora) == "Error" or verificarMinuto(minutos) == "Error" or verificarSegundos(segundos) == "Error":
        return print("Error")
    else:
        imprimir(hora, minutos, segundos)


#Agrupa las demás funciones para resolver el problema
def main():
    hora = int(input("Ingresa la hora: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))
    horaNueva = verificar(hora, minutos, segundos)

#Llama a la función principal para ser ejecutada
main()