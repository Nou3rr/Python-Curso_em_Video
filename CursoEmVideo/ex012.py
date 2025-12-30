#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = preco*.95

print(f"O preço do produto com desconto de 5% é R${desconto:.2f}")
