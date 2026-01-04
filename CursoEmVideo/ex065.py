#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maior = None
menor = None
media = 0
contador = 0

while True:
    numero = int(input("Digite um número ou 999 para sair: "))

    if numero != 999:
        media += numero
        contador += 1

        if maior is None or numero>maior:
            maior = numero
        if menor is None or numero<menor:
            menor = numero

    else:
        print(f"O maior número inserido foi {maior}")
        print(f"O menor número inserido foi {menor}")
        print(f"A média dos números inseridos foi {media/contador}")
