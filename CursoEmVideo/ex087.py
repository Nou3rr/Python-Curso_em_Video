#Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = None

for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um número para [{linha},{coluna}]: "))
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if linha == 1:
            if maior_valor_segunda_linha is None:
                maior_valor_segunda_linha = matriz[linha][coluna]
            elif matriz[linha][coluna] > maior_valor_segunda_linha:
                maior_valor_segunda_linha = matriz[linha][coluna]

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]",end="")
    print()
print()
print(f"A soma de todos os valores pares digitados é: {soma_pares} ")
print(f"A soma dos valores da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {maior_valor_segunda_linha}")