#Crie um programa que leia o nome completo de uma pessoa e mostre: – O nome com todas as letras maiúsculas e minúsculas. – Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
from gettext import find

nome = input("Digite seu nome completo: ")
nome_separado = nome.split()
print(f"Nome em maiúsculas {nome.upper()}")
print(f"Nome em minúsculas {nome.lower()}")
print(f"O nome completo tem {len(nome)-nome.count(' ')} letras")
print(f"O primeiro nome tem {len(nome_separado[1])} letras")
