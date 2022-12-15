#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a fazer uma viagem {}km.'.format(dist))

if dist <= 200:
    passagem = dist*0.45
    print('E o preço da sua passagem é de R${:.2f}'.format(passagem))
else:
    passagem = dist*0.45
    print('E o preço da sua passagem é de R${:.2f}'.format(passagem))