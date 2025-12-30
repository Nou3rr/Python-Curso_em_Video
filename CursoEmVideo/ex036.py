#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = int(input("Insira o valor da casa: "))
salario = int(input("Insira o salário do comprador: "))
anos = int(input("Insira em quantos deseja financiar: "))

parcela = valor_casa/(anos*12)

if parcela > salario*0.3:
    print(f"Financiamento negado, a parcela de R${parcela:.2f} excede 30% do salário do comprador.")
else:
    print(f"Financiamento aprovado, com parcelas de R$ {parcela:.2f} que ficam abaixo de 30% do salário")
