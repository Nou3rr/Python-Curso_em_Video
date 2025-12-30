#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

print("JO-KEN-PO")
escolha_computador = randint(1,3)
escolha_jogador = int(input("Insira o digito para jogar:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n"))
if escolha_jogador == escolha_computador:
    print("Empate! O jogador e o computador fizeram a mesma escolha")
elif escolha_jogador == 1 and escolha_computador == 3 or escolha_jogador == 2 and escolha_computador == 1 or escolha_jogador == 3 and escolha_computador == 1:
    print("O jogador venceu!")
else:
    print("O computador venceu")