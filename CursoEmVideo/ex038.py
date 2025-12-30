#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior – O segundo valor é maior – Não existe valor maior, os dois são iguais

numero_a = int(input("Digite um número: "))
numero_b = int(input("Digite outro número: "))

if numero_a > numero_b:
    print(f"{numero_a} é maior que {numero_b}")
elif numero_b > numero_a:
    print(f"{numero_b} é maior que {numero_a}")
elif numero_a == numero_b:
    print(f"{numero_a} e {numero_b} são iguais")