# Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = menor = media = soma = cont = 0
continuar = 'S'
while continuar not in 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = soma = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
