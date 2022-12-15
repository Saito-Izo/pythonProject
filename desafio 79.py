#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
resp = ''
while True:
    n = (int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso.')

    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado. Não vou adicionar...')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

valores.sort() #coloca os numeros em ordem
print(f'Você digitou os valores {valores}.')