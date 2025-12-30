#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

ano_atual = datetime.now().year
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade = ano_atual-ano_nascimento

if idade == 18:
    print(f"{idade} anos é a idade de alistamento obrigatório.")
elif idade < 18:
    print(f"{idade} anos ainda não é idade suficiente para se alistar. Volte em {18-idade} anos.")
elif idade > 18:
    print(f"Você está {idade-18} anos atrasado, se aliste imediatamente.")

