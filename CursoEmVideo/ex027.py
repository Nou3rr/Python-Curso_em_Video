#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite um nome completo: ").split()
print(f"{nome[0]}\n{nome[-1]}")