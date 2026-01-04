#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

notas50 = 0
notas20 = 0
notas10 = 0
notas01 = 0

saque = int(input("Digite o valor que deseja sacar:\n"))

while saque >0:

    if saque >= 50:
        notas50 += 1
        saque -= 50
    elif saque >= 20:
        notas20 += 1
        saque -= 20
    elif saque >= 10:
        notas10 += 1
        saque -= 10
    else:
        notas01 += 1
        saque -= 1

print(f"Notas R$ 50,00: {notas50} notas")
print(f"Notas R$ 20,00: {notas20} notas")
print(f"Notas R$ 10,00: {notas10} notas")
print(f"Notas R$ 1,00: {notas01} notas")