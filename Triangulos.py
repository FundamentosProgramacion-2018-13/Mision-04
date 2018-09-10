#Emiliano Heredia A01377072
#Dado 3 medidas definir si existe un triangulo y que tipo de triangulo es
def main():
    a = int(input("Ingrese el valor de lado A: "))
    b = int(input("Ingrese el valor de lado B: "))
    c = int(input("Ingrese el valor de lado C: "))

    if(isExisting(a,b,c)):
        print("No existe el triangulo con las medidas %.2f, %.2f, %.2f" % (a,b,c))
    else:
        print("El triangulo con las medidas %.2f, %.2f, %.2f si existe" %(a,b,c))
        print("Es un triangulo %s" % definirTipoTria(a,b,c))


#Define que tipo de triangulo es.
def definirTipoTria(a,b,c):
    tipo = ""
    if(a==b==c):
        tipo = "Equilatero"
    elif(a==b or a==c or c==b):
        tipo = "Isoseles"
    elif((a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (a**2)+(b**2)==(a**2)):
        tipo = "Rectangulo"
    else:
        tipo = "Irregular"
    return tipo


#Calcula si el triangulo existe
def isExisting(a,b,c):
    flag = False
    flag = False if (a+b>c and a+c>b and b+c>a) else True
    return flag


main()