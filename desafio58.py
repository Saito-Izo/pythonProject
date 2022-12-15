#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

from random import randint
from time import sleep
print('\33[1;31;43m-=-\33[m'*20)
print('\33[1;30;107mVou pensar em um número entre 0 e 10, tente advinhar.       \33[m')
print('\33[1;31;43m-=-\33[m'*20)
n = int(input('Em que número pensei? '))
num = randint(0,10)
palpite = 1

print('PROCESSANDO...')
sleep(1)

while n != num:
    if n < num:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    n = int(input('Em que número pensei? '))
    palpite += 1
if n==num:
    if palpite == 1:
        print(f'\33[0;30;42mPARABÉNS! Você acertou de primeira. \33[m')
    else:
        print(f'\33[0;30;42mPARABÉNS! Você acertou com {palpite} tentativas. \33[m')
