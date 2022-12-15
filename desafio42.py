#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo ', end='') #aqui o end é para imprimir o resultado ao lado da frase
    if a == b == c:
        print('EQUILÁTERO.')
    elif a != b != c != a: #é preciso colocar mais uma desigualdade no final para que 'a' seja diferente de 'c'.
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')

else:
    print('Os segmentos acima não podem formar um triângulo.')

