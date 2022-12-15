#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

print('_'*30)
print('CADASTRE UMA PESSOA')
print('_'*30)
id = homem = mulher = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        id += 1
    if id <= 20 and sexo == 'F':
        mulher += 1
    if sexo == 'M':
        homem += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais 18 anos: {id}\n'
              f'Ao todo temos {homem} homens cadastrados.\n'
              f'E temos {mulher} mulheres com menos de 20 anos.')