galera = list()
dado = list()
totalmaior = totalmenor = 0

for c in range (0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # [:] faz cópia da lista dado em galera
    dado.clear() # apaga os dados da lista 'dado'

for p in galera:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totalmenor += 1

print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')