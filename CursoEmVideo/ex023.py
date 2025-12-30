#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# numero = int(input("Digite um número de 0 a 9999: "))
# numero_string = str(numero)
# if 0 <= numero <= 9999:
#     if numero < 10:
#         print(f"{numero_string[0]} unidade(s)")
#     elif 10 <= numero <= 100:
#         print(f"{numero_string[0]} dezena(s)\n{numero_string[1]} unidade(s)")
#     elif 100 <= numero <= 1000:
#         print(f"{numero_string[0]} centena(s)\n{numero_string[1]} dezena(s)\n{numero_string[2]} unidade(s)")
#     else:
#         print(f"{numero_string[0]} milhar(es)\n{numero_string[1]} centena(s)\n{numero_string[2]} dezena(s)\n{numero_string[3]} unidade(s)")

numero = int(input("Digite um número de 0 a 9999: "))

if 0 <= numero <= 9999:
    unidade = numero // 1 % 10 #O resto adiciona tudo que fica além da vírgula
    dezena = numero // 10 % 10
    centena = numero // 100 % 10
    milhar = numero // 1000 % 10

    print(f"Unidade {unidade}")
    print(f"Dezena {dezena}")
    print(f"Centena {centena}")
    print(f"Milhar {milhar}")
else:
    print("O número inserido está fora do alcance dos valores estipulados.")
