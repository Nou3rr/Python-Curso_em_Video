#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#  à vista dinheiro/cheque: 10% de desconto – à vista no cartão: 5% de desconto – em até 2x no cartão: preço formal – 3x ou mais no cartão: 20% de juros

preco = float(input("Digite o preço do produto: "))
pagamento = int(input("Digite o número de parcelas em que deseja realizar o pagamento: "))

if pagamento == 1:
    print(f"Pagamento à vista com desconto de 10%: R${preco*0.9:.2f}")
elif pagamento == 2:
    print(f"Pagamento em até 2x, sem juros: R${preco:.2f} ")
elif pagamento > 2:
    print(f"Pagamento em {pagamento}x, com 20% de juros: R$ {preco*1.2:.2f}")