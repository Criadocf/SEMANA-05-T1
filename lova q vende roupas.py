#Você é dono de uma loja que vende roupas. Sua política é de dar desconto para quem compra à
#vista, vender pelo preço de etiqueta para quem paga em 5 vezes e cobrar jutos de quem comprar
#em 10 vezes. Escreva um programa que leia o valor de uma compra e imprima três valores, todos
#com até duas casas decimais:
#• Valor para pagamento à vista, com desconto de 9%.
#• Valor da prestação para pagamento em 5 vezes, sem desconto nem juros.
#• Valor da prestação para pagamento em 10 vezes, com 17% de juros.

def valor(x):
    viz = x*(0.91)
    cin = x
    dez = x*(1.17)
    return viz, cin, dez

val = float(input())

x, y, z = valor(val) 


print (f'R${x:.2f}\nR${y:.2f}\nR${z:.2f}')
    
    



