#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

classe = []

while True:
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1+nota2) / 2
    classe.append([nome,[nota1,nota2],media])
    continuar = input("Quer continuar? [S/N]: ").lower().strip()
    if continuar != "s":
        break

print("-="*16)
print("No.",f"{'NOME':<20}", "MÉDIA")
print("-"*32)
for i, aluno in enumerate(classe):
    print(f"{i:<3}",f"{aluno[0]:<20}",f"{aluno[2]}")

while True:
    mostrar_notas = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if mostrar_notas == 999:
        print("FINALIZANDO...")
        break
    elif mostrar_notas < len(classe):
        print(f"As notas de {classe[mostrar_notas][0]} são {classe[mostrar_notas][1]}")
    else:
        print(f"Código de aluno fora do limite! Insira um número entre 0 e {len(classe)}")
print(f"<<< VOLTE SEMPRE >>>")