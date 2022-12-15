#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça
#para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

decimal = int(input('Digite um número inteiro: '))
print('''Escolha uma das base para a conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL''')

escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(decimal, bin(decimal)[2:]))

elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(decimal, oct(decimal)[2:]))

elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(decimal, hex(decimal)[2:]))

else:
    print('Opção inválida. Tente novamente.')