#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

jogos = []
temporaria = []

print("-"*30)
print(f"{'JOGOS NA MEGA SENA':^30}")
print("-"*30)

quantidade_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print("=-"*3,f"{'SORTEANDO JOGOS':^18}","-="*3)

for j in range(0,quantidade_jogos):
    while len(temporaria) < 6:
        numero = randint(1,60)
        if numero not in temporaria:
            temporaria.append(numero)
    temporaria.sort()
    jogos.append(temporaria[:])
    temporaria.clear()

for iteracao,jogo in enumerate(jogos):
    sleep(0.5)
    print(f"Jogo {iteracao+1}: {jogo}")


print("=-"*4, "< BOA SORTE >", "-="*4)