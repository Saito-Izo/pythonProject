#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('\33[1;31;43m-=-\33[m'*20)
print('\33[1;30;107mVou pensar em um número entre 0 e 5, tente advinhar.        \33[m')
print('\33[1;31;43m-=-\33[m'*20)
n = int(input('Em que número pensei? '))
num = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if n==num:
    print('\33[0;30;42mPARABÉNS! Você conseguiu me vencer! \33[m')
else:
    print('\33[0;30;41mGANHEI! Eu pensei no número {} e não no {} \33[m'.format(num,n))