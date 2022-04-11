# Escreva um programa que leia o tempo de duração de um evento em uma
# fábrica expresso em segundos. Calcule e exiba esse tempo em horas,
# minutos e segundos (HH:MM:SS)
    
def segundos(x):
    h = x // 3600
    m = x // 60 - h*60
    s = x - m*60 - h*3600
    return h,m,s

seg = int(input())

ch = segundos(seg)

print(ch)





