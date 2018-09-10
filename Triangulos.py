# Autor: Silvia Ferman Muñoz
# Programa que lee los lados de un triángulo
# Tecnica Top-Down


# Checar que tipo de TRIANGULO ES
def checarTipoTriangulo(A, B, C):
     if (A > B) and (A > C):
         return "Es un Triangulo Rectángulo"
     if (A == B) or (B == C) :
         return "Es un Triangulo Isóceles"
     if (A == B) and (B == C):
          return "Es un Triángulo Equilatero"
     else:
         return "Estos lados no corresponden a un triángulo"


# Función principal
def main():
     A = int(input("El lado A vale: "))
     B = int(input("El lado B vale: "))
     C = int(input("El lado C vale: "))

     print(checarTipoTriangulo(A, B, C))


# Llama a la función principal
main()