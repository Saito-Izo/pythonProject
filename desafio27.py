#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))

#a função len mostra a quantidade exata de caracteres, porém, no que diz respeito à posição a contagem começa do zero.
#Portanto, é preciso subtrair 1 quando usado len para obter a posição desejada.
#no print abaixo: [len(nome)-1] é um número.
print('Seu último nome é {}'.format(nome[len(nome)-1]))