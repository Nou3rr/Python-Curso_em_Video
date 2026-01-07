# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.
from itertools import count
from operator import index

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))

tupla = (n1,n2,n3,n4)

if 9 in tupla:
    print(f"O valor 9 apareceu {tupla.count(9)} vezes")
else:
    print("O valor 9 não foi inserido")

if 3 in tupla:
    print(f"O valor 3 apareceu pela primeira vez na {tupla.index(3)+1}ª posição")
else:
    print(f"O valor 3 não foi inserido")

print("Os números pares inseridos foram:")
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=" ")