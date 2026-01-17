#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.

temporaria = []
pessoas = []
peso_mais_pesado = peso_mais_leve = 0
pessoas_mais_pesadas = []
pessoas_mais_leves = []

while True:
    temporaria.append(input("Nome: "))
    temporaria.append(float(input("Peso: ")))
    pessoas.append(temporaria[:])

    if len(pessoas) == 1:
        peso_mais_pesado = peso_mais_leve = temporaria[1]
    temporaria.clear()

    continuar = input("Para continuar inserindo nomes e pesos, digite S, ou qualquer outra para encerrar o programa.\n").strip().lower()
    if continuar != "s":
        break

#condição de manipulação da pessoa mais pesada
for pessoa, peso in pessoas:
    if peso > peso_mais_pesado:
        pessoas_mais_pesadas.clear()
        peso_mais_pesado = peso
        pessoas_mais_pesadas.append(pessoa)
    elif peso == peso_mais_pesado:
        pessoas_mais_pesadas.append(pessoa)

#condição de manipulação da pessoa mais leve
    if peso < peso_mais_leve:
        pessoas_mais_leves.clear()
        peso_mais_leve = peso
        pessoas_mais_leves.append(pessoa)
    elif peso == peso_mais_leve:
        pessoas_mais_leves.append(pessoa)

print(f"Foram cadastradas {len(pessoas)} pessoas")
print(f"A pessoa cadastrada com o maior peso foi {', '.join(pessoas_mais_pesadas)} com {peso_mais_pesado:.2f} kg")
print(f"A pessoa cadastrada com o menor peso foi {', '.join(pessoas_mais_leves)} com {peso_mais_leve:.2f} kg.")
