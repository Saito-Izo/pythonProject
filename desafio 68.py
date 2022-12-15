#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
#quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
print(f'=-'*15)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print(f'=-'*15)
c = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = computador + jogador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? ')).strip().upper()[0] #O [0] torna maiuscula somente a primeira letra

    print(f'Você jogou {jogador} e o computador {computador}. Total deu {total}')
    if escolha == 'P' and total%2 == 0:
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        c += 1
    elif escolha == 'I' and total%2 != 0:
        print('Você VENCEU!\n'
              'Vamos jogar novamente...')
        c += 1
    else:
        print('Você PERDEU!')
        print('=-'*15)
        print(f'GAME OVER! Você venceu {c} vezes.')
        break