#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Ano de nascimento: '))
sexo = int(input('Informe o seu sexo, digite (1) para masculino ou (2) para feminino: '))
atual = date.today().year
d = atual - ano
alis = atual + (18 - d)
if sexo == 1:
    print('Quem nasceu em {} tem {} anos em {}.'.format(ano, d, atual))

    if d < 18:
        print('Ainda faltam {} anos para o alistamento.\n'
          'Seu alistamento será em {}.'.format(18-d, alis))

    elif d > 18:
        print('Você já deveria ter se alistado há {} anos.\n'
          'Seu alistamento foi em {}.'.format(d-18,alis))

    else:
        print('Você tem que se alistar IMEDIATAMENTE!')

elif sexo == 2:
    print('Não há alistamento obrigatório para pessoas do sexo feminino.')

else:
    print('Opção inválida, digite (1) ou (2) para informar o sexo')