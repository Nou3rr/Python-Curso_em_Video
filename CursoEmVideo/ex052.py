#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input("Digite um número: "))
contador = 0

for i in range(0,numero+1):
    if numero % (i+1) == 0:
        contador +=1
    if contador > 2:
        print(f"{numero} não é um número primo")
        break
if contador <= 2:
    print(f"{numero} é um número primo")