# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)


escreva('Izadora Yuna Nabhan Saito')
escreva('Francielly Soares Nabhan Costa Saito')
escreva('Izo Kiyoharu Saito Junior')