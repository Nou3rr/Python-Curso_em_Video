#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Digite o valor atual: "))
dolar = real/5.42

print(f"Você tem R${real}, com essa quantia pode comprar U${dolar:.2f}")