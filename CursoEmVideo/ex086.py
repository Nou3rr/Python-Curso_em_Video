#Crie um programa que declare uma matriz de dimensão 3 × 3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0,0,0],[0,0,0],[0,0,0]]

#percorre cada linha da matriz
for linha in range(0,3):
    #percorre cada coluna de indice da matriz
    for coluna in range(0,3):
        #preenche cada indice com um número inteiro
        matriz[linha][coluna] = int(input(f"Digite um número para a posição [{linha},{coluna}]: "))

print("-="*30)
#percorre cada linha da matriz
for linha in range(0,3):
    #percorre cada coluna de índice da matriz
    for coluna in range(0,3):
        #imprime na tela o número de cada indice centralizado em 5 espaços
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()