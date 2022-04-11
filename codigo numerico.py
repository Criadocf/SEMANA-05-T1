# 2 - Escreva um programa que leia um único caractere pelo teclado e
# informe o código numérico correspondente ao caractere lido.

def carac(x):
    return ord(x)

cod = input()

ch = carac(cod)

print(ch)