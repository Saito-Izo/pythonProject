#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = menor = 0
for pessoa in range(0, 5):
    peso = float(input(f'Peso da {pessoa + 1}ª pessoa: '))
# na primeira ocorrência as variáveis maior e menor recebem o mesmo valor.
    if pessoa == 0:
        menor = maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg.')
