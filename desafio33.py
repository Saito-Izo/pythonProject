#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#verificando o menor valor
menor = a
if a>c and b>c:
    menor = c

if a>b and c>b:
    menor = b

#verificando o maior valor
maior = a

if a<c and b<c:
    maior = c
if a<b and c<b:
    maior = b

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))