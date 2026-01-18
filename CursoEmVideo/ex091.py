#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadores = {}
jogadores['jogador1'] = randint(1,6)
jogadores['jogador2'] = randint(1,6)
jogadores['jogador3'] = randint(1,6)
jogadores['jogador4'] = randint(1,6)

for key, value in jogadores.items():
    print(f"O {key} tirou {value} no dado")

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("-="*15)
print("== RANKING DOS JOGADORES ==")
for indice, jogador in enumerate(ranking):
    print(f"{indice+1}º lugar: {jogador[0]} com {jogador[1]}")
