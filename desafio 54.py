# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
maior = menor = 0
print(f'O ano atual é {atual}')

for c in range(0, 7):
    ano = int(input(f'Em que ano a {c+1}ª pessoa nasceu? '))
    if atual - ano < 18:
        menor += 1
    else:
        maior += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')
