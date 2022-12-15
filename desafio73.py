#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato
# Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Santos.
# data do exercicio: 2022/09/27

times = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo', 'Corinthians', 'Athletico-PR', 'Athletico-MG',
         'América-MG', 'Goiás', 'São Paulo', 'Botafogo', 'Santos', 'Bragantino', 'Fortaleza', 'Ceará SC', 'Coritiba',
         'Avaí', 'Cuiabá', 'Athlético-GO', 'Juventus')

print('-='*30)
print(f'Lista de times do brasileirão em 2022: {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 ultimos são: {times[-4:]}') #times[-4:] indica os 4 de trás para frente.
print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}') #mostra em ordem, porém não muda as posições