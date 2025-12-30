#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

distancia = float(input("Insira a distância percorrida em quilômetros pelo veículo: "))
dias = int(input("Insira quantos dias o carro foi alugado: "))
total = (distancia*.15)+(dias*60)

print(f"O carro percorreu {distancia:.2f}km em {dias} dias. O valor total do aluguel é R${total:.2f}")