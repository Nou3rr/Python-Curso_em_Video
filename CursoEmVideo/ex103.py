#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(x,y):
    """
    :param x: onde é inserido o nome do jogador, caso não haja entrada será preenchido com Desconhecido
    :param y: onde é inserido o número de gols do jogador, caso não haja entrada válida o total será zero gols
    :return:
    """

    if len(x.strip()) == 0:
        x = "Desconhecido"
    if y.isdigit():
        y = int(y)
    else:
        y = 0
    print (f"O jogador {x} fez {y} gol(s) no campeonato.")


nome = input("Nome do Jogador: ")
gols = input("Número de Gols: ")

ficha(nome,gols)
