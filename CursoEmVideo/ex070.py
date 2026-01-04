# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.

total = 0
mais_de_mil = 0
nome_mais_barato = None
valor_mais_barato = None

while True:
    continuar = input("Digite [s] para cadastrar mais produtos ou qualquer outra tecla para encerrar o programa:\n").lower().strip()
    if continuar == "s":

        nome = input("Digite o nome do produto: ")
        valor = float(input("Digite o valor do produto: R$"))
        total += valor

        if nome_mais_barato is None:
            nome_mais_barato = nome
            valor_mais_barato = valor

        elif valor < valor_mais_barato:
            nome_mais_barato = nome
            valor_mais_barato = valor

        if valor > 1000:
            mais_de_mil += 1

    else:
        print("----- Programa Encerrado -----")
        print(f"O valor total da compra é R${total:.2f}")
        print(f"{mais_de_mil} itens que custam acima de R$1000,00 foram adicionados")
        print(f"O produto registrado com o menor valor foi {nome_mais_barato}")
        break