#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.
from itertools import count

lista = []

while True:
    numero = int(input("Digite um número ou 999 para encerrar o programa: "))
    if numero == 999:
        break
    else:
        lista.append(numero)

print(f"A lista contém {len(lista)} objetos")
print(f"A lista com valores em ordem decrescente é: {sorted(lista,reverse=True)}")
if 5 in lista:
    print(f"O número 5 foi encontrado {lista.count(5)} vezes")