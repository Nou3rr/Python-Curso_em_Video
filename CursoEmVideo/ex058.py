#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

num_computador = randint(1,10)
contador = 0

print("O computador irá escolher um número entre 1 e 10")
sleep(1)
print("Pronto!")

while True:
    num_jogador = int(input("Advinhe o número que o computador escolheu: "))
    if num_jogador == num_computador:
        contador += 1
        print(f"O número correto é {num_computador}\nO jogador advinhou em {contador} jogadas.")
        break
    else:
        print("Errou!, tente outra vez")
        contador += 1