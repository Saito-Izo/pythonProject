#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
res = 0
opcao = 0
app = True
while app:
    opcao = int(input('     [ 1 ] somar\n'
                      '     [ 2 ] multiplicar\n'
                      '     [ 3 ] maior\n'
                      '     [ 4 ] novos números\n'
                      '     [ 5 ] sair do programa\n'
                      '>>>>> Qual é a sua opção? '))
    if opcao == 1:
        res = num1 + num2
        print(f'A soma entre {num1} e {num2} é {res}.')
        print('=-='*10)
    elif opcao == 2:
        res = num1*num2
        print(f'O produto de {num1} e {num2} é {res}.')
        print('=-=' * 10)
    elif opcao == 3:
        if num1 > num2:
            print(f'Entre {num1} e {num2} o maior valor é {num1}.')
            print('=-=' * 10)
        else:
            print(f'Entre {num1} e {num2} o maior valor é {num2}.')
            print('=-=' * 10)
    elif opcao == 4:
        print('Informe os números novamente:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('=-=' * 10)

    elif opcao == 5:
        app = False
    elif opcao > 5 or opcao < 1:
        print('Opção inválida. Tente novamente.')
        print('=-=' * 10)
print('Finalizando...')
sleep(2)
print('=-='*10)
print('Fim do programa! Volte Sempre!')