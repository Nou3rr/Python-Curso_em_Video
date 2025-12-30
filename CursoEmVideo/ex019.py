#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

aluno1 = input("Nome do aluno 1: ")
aluno2 = input("Nome do aluno 2: ")
aluno3 = input("Nome do aluno 3: ")
aluno4 = input("Nome do aluno 4: ")

sorteado = choice([aluno1, aluno2, aluno3, aluno4])

print(f"O aluno sorteado foi {sorteado}!")
