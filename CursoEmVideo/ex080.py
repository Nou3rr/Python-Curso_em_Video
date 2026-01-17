#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = list()
index = 0

for i in range(0,5):
    numero = int(input("Digite um número: "))
    if i == 0 or numero > lista[-1]:
        lista.append(numero)
        print("O número foi inserido ao final da lista")
    else:
        while index < len(lista):
            if numero <= lista[index]:
                lista.insert(index, numero)
                print(f"Adicionado na posição {index} da lista")
                break
            index += 1
print("=-"*30)
print(f"Os valores digitados na lista foram {lista}")
