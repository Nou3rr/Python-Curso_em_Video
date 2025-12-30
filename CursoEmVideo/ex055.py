#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(0,5):
    peso = int(input(f"Digite o peso da pessoa {i+1}: "))
    if peso > maior:
        maior = peso
    if menor == 0 or peso < menor:
        menor = peso

print(f"O menor peso é {menor}KG e o maior peso é {maior}KG")