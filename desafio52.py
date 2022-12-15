#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
tot = 0 #variável para contar os números divisores
for c in range (1, n+1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1 # ou tot = tot + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('Portanto é número primo.')
else:
    print('Portanto não é número primo.')