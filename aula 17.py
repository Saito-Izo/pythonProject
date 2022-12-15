valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for a, b in enumerate(valores):
    print(f'Na posição {a} encontrei o valor {b}.')
print('Cheguei ao final da lista.')