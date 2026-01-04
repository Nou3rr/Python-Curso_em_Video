#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número qualquer ou 999 para sair: "))
    if numero != 999:
        soma += numero
        quantidade += 1
    else:
        print(f"Você inseriu:\n{quantidade} números\nE a soma total entre eles é {soma}\n---- ENCERRANDO PROGRAMA ----")
        break
