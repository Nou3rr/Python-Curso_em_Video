#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input("Digite uma frase: ").strip()
frase_inversa = ""
frase_sem_espaço = ""

for caractere in frase[::-1]:
    if caractere == " " or ",":
        continue
    else:
        frase_inversa = frase_inversa+caractere

for caractere in frase:
    if caractere == " " or ",":
        continue
    else:
        frase_sem_espaço = frase_sem_espaço+caractere

if frase_sem_espaço == frase_inversa:
    print(f"A frase '{frase}' é um palíndromo!")
else:
    print(f"A frase '{frase}' não é um palíndromo!")
