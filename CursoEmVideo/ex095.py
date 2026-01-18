# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []
cod = 0

while True:
    jogador = {'cod': 0, 'nome': str(input("Nome do jogador: ")), 'gols': [], 'total': 0}
    qt_partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    for partida in range(0,qt_partidas):
        gols = int(input(f"   Quantos gols na partida {partida+1}? "))
        jogador['gols'].append(gols)
        jogador['total'] += gols
        jogador['cod'] = cod
    time.append(jogador.copy())
    cod += 1
    while True:
        continuar = input("Deseja continuar? [S/N] ").lower().strip()
        if continuar not in "sn":
            print("ERRO! Digite apenas S ou N")
        else:
            break
    if continuar == "n":
        break

print("-="*30)
print(f"cod ", f"{'nome':<20}", f"{'gols':<20}", f"{'total':^10}")
print("-"*60)
for dicionario in time:
    print(f"{dicionario['cod']:>3}", f" {dicionario['nome']:<20}", f"{str(dicionario['gols']):<22}", f"{dicionario['total']:<10}")

while True:
    mostrar_dados = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if mostrar_dados == 999:
        break
    elif mostrar_dados <= len(time)-1:
        print(f" -- LEVANTAMENTO DO JOGADOR {time[mostrar_dados]['nome']}")
        for partida, gol in enumerate(time[mostrar_dados]['gols']):
            print(f"No jogo {partida+1} fez {gol} gols.")