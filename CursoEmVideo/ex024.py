#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input("Digite o nome de uma cidade: ").lower().split()
if "santo" in cidade[0]:
    print("A cidade começa com Santo!")
else:
    print("A cidade não começa com Santo!")
