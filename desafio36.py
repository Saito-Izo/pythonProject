# Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento? '))

mes = ano*12
prest = casa/mes
ps = sal*30/100

print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, ano, prest))

if prest > ps:
    print('Empréstimo NEGADO')

else:
    print('Empréstimo pode ser CONCEDIDO')