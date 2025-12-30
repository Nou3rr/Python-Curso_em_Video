#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input("Digite um número: "))
conversao = int(input("Conversor, digite:\n[1] - binário\n[2] - octal\n[3] - hexadecimal\n"))

if conversao == 1:
    print(f"{numero} convertido para binário é {bin(numero)[2:]}")
elif conversao == 2:
    print(f"{numero} convertido para octal é {oct(numero)[2:]}")
elif conversao == 3:
    print(f"{numero} convertido para hexadecimal é {hex(numero)[:2]}")
else:
    print("Entrada inválida!\nPROGRAMA ENCERRADO")