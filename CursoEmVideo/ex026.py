#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ").lower()
print(f"A frase tem {frase.count('a')} letras A")
print(f"A primeira vez que a letra A aparece na frase é na posição {frase.find('a')+1}")
print(f"A última vez que a letra A aparece na frase é na posição {frase.rfind('a')+1}")