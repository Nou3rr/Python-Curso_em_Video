#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {'nome':'vazio','gols':[],'total':0}
jogador['nome'] = str(input("Nome do jogador: "))

qt_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
for partida in range(0,qt_partidas):
    gols = int(input(f"   Quantos gols na partida {partida}? "))
    jogador['gols'].append(gols)
    jogador['total'] += gols

print("-="*30)
print(jogador)
print("-="*30)
for key, value in jogador.items():
    print(f"O campo {key} tem o valor {value}")
print("-="*30)
print(f"O jogador {jogador['nome']} jogou {qt_partidas} partidas.")
for partida in range(0,qt_partidas):
    print(f"    => Na partida {partida}, fez {jogador['gols'][partida]}")
print(f"Um total de {jogador['total']} gols")
