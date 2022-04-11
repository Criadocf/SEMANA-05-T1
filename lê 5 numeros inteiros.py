# Escreva um programa/algoritmo que leia 5 (cinco) números inteiros e escreva na tela:
# • o maior número lido;
# • o menor número lido;
# • a média aritmética dos números lidos.

 
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())

media = float((num1+num2+num3+num4+num5)/5)

print (max(num1, num2, num3, num4, num5))
print(min(num1, num2, num3, num4, num5))
print(f'{media:.1f}')




    



    