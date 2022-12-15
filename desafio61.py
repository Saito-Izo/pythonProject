#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
# termos da progressão usando a estrutura while.
print('Gerador de PA')
print('-=' * 10)
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
a = n
contador = 1
while contador <= 10:
    print(f'{a}', end=' → ')
    a = n + r
    n += r
    contador += 1
print('FIM')

