#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input("Digite um nome: ").lower()
if "silva" in nome:
    print("Você faz parte da família Silva!")
else:
    print("Você não faz parte da família Silva.")
