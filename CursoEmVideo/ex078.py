#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = list()
maior = None
menor = None

for n in range(0,5):
    lista.append(int(input("Digite um número: ")))

for num in lista:
    if maior is None and menor is None:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

print(f"{maior} foi o maior número inserido e aparece na posição: ",end="")
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f"...{indice}", end=" ")

print(f"\n{menor} foi o menor número inserido e aparece na posição: ",end="")
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f"...{indice}", end=" ")
