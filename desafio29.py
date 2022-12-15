#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual a velocidade atual do carro? '))
if v>80:
    print('\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80km/h.\n'
          'Você deve pagar uma multa de\033[m \033[1;33mR$280,00\033[m\033[31m.\n'
          '\033[1;33mTenha um bom dia! Dirija com segurança.\033[m')
else:
    print('\033[1;33mTenha um bom dia! Dirija com segurança.\033[m')