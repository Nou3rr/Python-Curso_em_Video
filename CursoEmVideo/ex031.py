#Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia_viagem = int(input("Insira a distância da viagem em quilômetros: "))
if distancia_viagem <= 200:
    valor_viagem = distancia_viagem*0.5
    print(f"O valor da viagem é R$ {valor_viagem:.2f}")
else:
    valor_viagem = distancia_viagem*0.45
    print(f"O valor da viagem é R${valor_viagem:.2f}")