#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {'nome': str(input("Nome: ")),'média':float(0)}
aluno['média'] = float(input(f"Digite a média de {aluno['nome']}: "))
if aluno['média'] < 5:
    aluno['situação'] = "Reprovado"
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = "Recuperação"
else:
    aluno['situação'] = "Aprovado"
print("-="*30)
for key, value in aluno.items():
    print(f"{key} é igual a {value}")
