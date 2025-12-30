#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

menores = 0
maiores = 0

for i in range(0,7):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Existem {menores} menores e {maiores} maiores de idade.")
