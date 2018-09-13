# Autor: Juan Sebastián Lozano Derbez
# Convierte la hora de formato de 24 a formato de 12

def convertirHora(horas):                   #Serie de ifs en las que se determina si la hora está en formato de 24 hrs, si sí lo está, le resta 12. También se establece que si la hora es 24, será igual a 0
    if horas > 12 and horas <= 23:
        horas = horas - 12
        return horas
    else:
        if horas <= 12 and horas >=0:
            return horas
        else:
            if horas == 24:
                horas = 0
                return horas

def main():                             #Se recibe la hora y se ejecuta la función siempre y cuando la hora sea válida
    hor = int(input("Horas: "))
    min = int(input("Minutos: "))
    seg = int(input("Segundos: "))

    if hor > 24 and hor < 1:
        print("Error")
    else:
        if hor > 0 and hor < 25:
            horas = convertirHora(hor)
            print(horas,':',min,':',seg, sep='')

main()