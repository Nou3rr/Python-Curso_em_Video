#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

numero_computador = randint(0,5)
print("Escolhendo um número...")
sleep(0.5)
print("...")
sleep(0.5)
numero_usuario = int(input("Certo, já escolhi meu número! Entre 0 e 5, tente adivinhar qual eu escolhi: "))

if numero_computador == numero_usuario:
    print(f"Parabéns! Você acertou! O número que escolhi foi {numero_computador}!")
else:
    print(f"Não foi dessa vez, o número que escolhi foi {numero_computador}")
