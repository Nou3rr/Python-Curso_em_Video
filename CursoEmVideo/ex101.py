#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import datetime

def voto(x):
    """
    Função que dirá qual o dever de voto da pessoa com base na sua idade.
    :param x: Ano de nascimento da pessoa
    :return: Situação de obrigatoriedade de voto
    """
    idade = datetime.now().year - x

    if 16 <= idade < 18 or idade >= 65:
        return f"Com {idade} anos: Voto opcional."
    elif 18 <= idade < 65:
        return f"Com {idade} anos: Voto obrigatório."
    else:
        return f"Com {idade} anos: Não vota."

print("-"*30)
idade = int(input("Em que ano você nasceu? "))
print(voto(idade))