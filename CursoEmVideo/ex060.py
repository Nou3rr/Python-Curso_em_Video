#Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("Digite um número: "))
fatorial = numero
numero_referencia = numero

while numero > 1:
    fatorial *= numero-1
    numero -= 1

print(f"O fatorial de {numero_referencia} é {fatorial}")