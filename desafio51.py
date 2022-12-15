#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = (n + (10-1) * r) + r
for c in range(n, decimo, r):
    print('{}'.format(c), end=' → ')
print('ACABOU')