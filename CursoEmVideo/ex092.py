#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

ficha = {}
ficha['nome'] = str(input("Nome: "))
ficha['idade'] = datetime.now().year - int(input("Ano de nascimento: "))
ficha['ctps'] = int(input("Carteira de trabalho (0 não tem): "))

if ficha['ctps'] != 0:
    ficha['contratação'] = int(input("Ano de contratação: "))
    ficha['salário'] = int(input("Salário: "))
    ficha['aposentadoria'] = 35 - (datetime.now().year - ficha['contratação'])
print("-=" * 30)
for key, value in ficha.items():
    print(f" - {key} tem o valor {value}")
