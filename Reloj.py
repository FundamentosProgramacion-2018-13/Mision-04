# Autor: Silvia Ferman Muñoz
# Programa que convierte las hora en formato de 24 hrs. al formato de 12 hrs.
# Tecnica Top-Down


# Convierte el formato 24hrs. al de 12hrs.
def convertirTiempo(horas,minutos,segundos):
     if (type(horas) == int) and (horas >= 0 and horas <= 23) and (type(minutos) == int) and (horas >= 0 and horas <= 60) and (type(segundos) == int) and (horas >= 0 and horas <= 60):
         if horas >= 12:
             pm = "pm"
             horas = horas - 12
         else:
             pm = "am"
         return "%02d:%02d:%02d %s" % (horas, minutos, segundos, pm)
     else:
         print("ERROR")


# Función principal
def main():
     horas = int(input("Horas: "))
     minutos = int(input("Minutos: "))
     segundos= int(input("Segundos: "))
     print(convertirTiempo(horas, minutos,segundos))


# Llama a la función principal
main()