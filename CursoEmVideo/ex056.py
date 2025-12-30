#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media = 0
mais_velho = 0
mulher_abaixo_de_20 = 0
nome_mais_velho = ""

for i in range(0,4):
    print(f"----- {i+1}ª PESSOA -----")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Gênero: [M/F]: ").lower()

    media += idade
    if sexo == "m":
        if mais_velho == 0 or idade > mais_velho:
            mais_velho = idade
            nome_mais_velho = nome

    if sexo == "f":
        if idade < 20:
            mulher_abaixo_de_20 += 1


print(f"O homem mais velho se chama {nome_mais_velho} e tem {mais_velho} anos")
print(f"A idade média do grupo é {media/4} anos")
print(f"Existem {mulher_abaixo_de_20} abaixo de 20 anos")
