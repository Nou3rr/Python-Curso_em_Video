#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JÚNIOR – Até 25 anos: SÊNIOR – Acima de 25 anos: MASTER

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = datetime.now().year-ano_nascimento

if idade <= 9:
    print(f"{idade} anos categoria MIRIM")
elif idade <= 14:
    print(f"{idade} anos categoria INFANTIL")
elif idade <= 19:
    print(f"{idade} anos categoria JÚNIOR")
elif idade <= 25:
    print(f"{idade} anos categoria SÊNIOR")
else:
    print(f"{idade} anos categoria MASTER")