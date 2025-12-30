#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import sample

aluno1 = input("Nome do aluno 1: ")
aluno2 = input("Nome do aluno 2: ")
aluno3 = input("Nome do aluno 3: ")
aluno4 = input("Nome do aluno 4: ")

ordem = sample([aluno1, aluno2, aluno3, aluno4],4)

print(f"A ordem de apresentação dos trabalhos é: {ordem}")

