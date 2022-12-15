dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

pag = dias*60+km*0.15

print('O total a pagar é de R${:.2f}'.format(pag))
