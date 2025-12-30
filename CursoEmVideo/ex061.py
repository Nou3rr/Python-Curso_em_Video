#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
PA = 0
contador = 0

while contador < 9:
    if PA == 0:
        print(termo)
        PA = termo+razao
        print(PA)
        contador += 1
    else:
        PA += razao
        print(PA)
        contador += 1
