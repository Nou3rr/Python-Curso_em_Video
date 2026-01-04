#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0

while True:
    numero_computador = randint(1,2)
    escolha_jogador = int(input("[1]Ímpar ou [2]Par? "))
    numeros_jogador = int(input("Que número você vai apostar? "))
    resultado = numeros_jogador+numero_computador

    if escolha_jogador == 1 and resultado % 2 == 1:
        print(f"Parabéns, você venceu! Você colocou {numeros_jogador} e computador {numero_computador}, o resultado {resultado} é ÍMPAR!")
        vitorias += 1

    elif escolha_jogador == 1 and resultado % 2 == 0:
        print(f"Você perdeu! Você colocou {numeros_jogador} e computador {numero_computador}, o resultado {resultado} é PAR!")
        print(f"Você teve {vitorias} vitorias")
        break

    elif escolha_jogador == 2 and resultado % 2 == 0:
        print(f"Parabéns, você venceu! Você colocou {numeros_jogador} e computador {numero_computador}, o resultado {resultado} é PAR!")
        vitorias += 1

    elif escolha_jogador == 2 and resultado % 2 == 1:
        print(f"Você perdeu! Você colocou {numeros_jogador} e computador {numero_computador}, o resultado {resultado} é ÍMPAR!")
        print(f"Você teve {vitorias} vitorias")

