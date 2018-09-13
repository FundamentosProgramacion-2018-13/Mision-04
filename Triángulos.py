#Damián Iván García Ravelo
#Programa que de acuerdo a los lados de un triángulo determina su tipo

def buscarTipoDeTriangulo (lado1, lado2, lado3):
#Función que busca el tipo de triángulo

    if lado1 <= 0 or lado2 <= 0 or lado3 <= 0: #Si recibe medidas negativas no busca el tipo de triángulo
        print("Ingrese medidas positivas")
    elif lado1 == lado2 and lado1 == lado3: #El equilátero tiene todos sus lados iguales
        print("El triángulo es equilátero")

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3: #El isóceles tiene 2 lados iguales
        print("El triángulo es isóceles")

    elif lado1 == ((lado2**2 + lado3**2)**0.5) or lado2 == ((lado1**2 + lado3**2)**0.5) or lado3 == ((lado1**2 + lado3**2)**0.5):
        print ("El triángulo es rectángulo") #El rectángulo se obtiene con teorema de pitágoras
    else:
        print("Las medidas no corresponden a un triángulo de estos tipos")

#Si se hacen en distintas funciones, el isóceles y el equilátero pueden salir como las mismas respuestas
#es por eso que a fuerzas se tienen que hacer en una misma declaración
def main():
#Pregunta al usuario los lados
    lado1 = float(input("Teclea el valor del primer lado: "))
    lado2 = float(input("Teclea el valor del segundo lado: "))
    lado3 = float(input("Teclea el valor del tercer lado: "))
#Imprime a la función
    tipoTriangulo = buscarTipoDeTriangulo(lado1, lado2, lado3)
    print(tipoTriangulo)

main()
