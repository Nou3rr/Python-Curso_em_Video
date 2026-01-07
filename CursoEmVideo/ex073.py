#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Bragantino.

times = ("Flamengo","Palmeiras","Cruzeiro","Mirassol","Fluminense","Botagofo","Bahia","São Paulo","Grêmio","Bragantino","Atlético-MG",
         "Santos","Corinthians","Vasco da Gama","EC Vitória","Internacional","Ceará SC","Fortaleza","Juventude","Sport Recife")

print("Os 5 primeiros colocados são:")
for x in range(0,5):
    print(f"{x+1}º {times[x]}")

print("\nOs últimos 4 colados são: ")
for y in range(20,16,-1):
    print(f"{y}º {times[y-1]}")

print("\nTimes em ordem alfabética")
for time in sorted(times):
    print(time)

print(f"\nO Bragantino está na {times.index('Bragantino')+1}ª posição ")

