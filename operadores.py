# Soma
def soma(a, b):
    print(f"\nO resultado da soma: {a + b}")

# Subtração
def sub(a, b):
    print(f"\nO resultado da subtração: {a - b}")

#  Multiplicação 
def multi(a, b):
    print(f"\nO resultado da multiplicação: {a * b}")

#  Divisão
def div(a, b):
    if b == 0:
        print("\nERRO, divisão por 0")
        return
    print(f"\nO resultado da divisão: {a / b}")

#  Potência
def potencia(a, b):
    print(f"\nO resultado da potência: {a ** b}")

#  Porcentagem
def porcent(a, b):
    print(f"\nO resultado da porcentagem: {(a * b) / 100}")

#  Raíz
def raiz(indice, numero):
    if numero < 0:
        print("\nERRO: raiz de número negativo!")
        return
    print(f"\nO resultado da raíz: {numero ** (1 / indice)}") 