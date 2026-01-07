#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ("Caderno", 30.99, "Apontador", 4.49, "Lápis", 0.9, "Caneta", 2.49, "Borracha", 1.2, "Corretivo", 5.90, "Estojo", 18.2)

print(f"{'Lista de Preços':-^39}")

for produto in range(0,len(produtos)):
    if produto % 2 == 0:
        print(f"{produtos[produto]:.<30}",end="")
    else:
        print(f"R${produtos[produto]:>7.2f}")