#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade_carro = int(input("Insira a velocidade que o carro percorria o trecho: "))
if velocidade_carro <= 80:
    print(f"{velocidade_carro}Kh/h esta dentro do limite da via.")
else:
    velocidade_excedente = velocidade_carro-80
    multa = velocidade_excedente*7
    print(f"{velocidade_carro}Km/h excede a velocidade permitida na via. Veículo multado em R$ {multa:.2f}.")