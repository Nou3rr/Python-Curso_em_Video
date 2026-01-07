#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

extenso = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if -1 < numero <= 20:
        print(f"Você digitou o número {extenso[numero]}")
        break
    else:
        print(f"Erro! Você digitou um número fora do intervalo (0 à 20). Tente novamente!")