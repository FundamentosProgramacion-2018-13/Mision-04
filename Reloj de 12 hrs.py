# Autor: Ithan Alexis Pérez Sánchez
# Convertición de hora en formato 24 Hrs.

# El codigo empieza después de esta linea

def convertir_Tiempo(Horas): # Se hace la conversión para determinar si cumple con el formato y sino que no mande un error
    if 1 <= Horas <= 24:
        return Horas % 12

def mantener_Tiempo(Minutos):
    if 0 <= Minutos <= 60:
        return Minutos

def mantener_Tiempo2 (Segundos):
    if 0 <= Segundos <= 60:
        return Segundos

def main(): # Manejar datos para que nosotros ingresemos y nos regrese como esta definido la hora.
    Horas = int(input("Escribe la hora: "))
    Minutos = int(input("Escribe los minutos: "))
    Segundos = int(input("Eacribe los segundos: "))
    Aviso = convertir_Tiempo(Horas), mantener_Tiempo(Minutos), mantener_Tiempo2(Segundos)
    print("La hora es: ", Aviso)

main()