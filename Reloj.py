#Autor: Diana Marisol Medina Bravo
#Lee  la hora, el minuto y el segundo.Convierte la hora en formato de 24 horas al formato de 12 hrs.


#Función para calcular la hora en formato 12hrs.
#Recibe la hora, los minutos y los segundos y regresa la hora en formato 12hrs.
def determinarHoraFormato12hrs(hora,minutos,segundos):
    if hora>12 and hora!=0 and hora<=24:
        horaFormato12= hora-12
        final="pm"
        return horaFormato12, minutos, segundos, final

    if hora<12 and hora>0:
       final="am"
       return hora, minutos, segundos, final


#Función principal
def main():
    hora= int(input("Ingrese la hora: "))
    minutos=int(input("Ingrese los minutos: "))
    segundos=int(input("Ingrese los segundos: "))

    if minutos<60 and segundos<60 and hora<=24 and hora!=0:
        (horaFormato, minutos, segundos, final) = determinarHoraFormato12hrs(hora, minutos, segundos)
        print (" ")
        print (horaFormato,":",minutos,":",segundos, final)
    else:
        print("Error")



main()