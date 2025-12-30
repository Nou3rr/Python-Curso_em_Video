#Melhore o DESAFIO 61 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
PA = 0
contador = 0

while True:
    if contador < 9:
        if PA == 0:
            print(termo)
            PA = termo+razao
            print(PA)
            contador += 1
        else:
            PA += razao
            print(PA)
            contador += 1
    else:
        continuar = input("Digite [s] para inserir novos termos ou qualquer outra tecla para encerrar o programa: ").strip().lower()
        if continuar == "s":
            termo = int(input("Digite o primeiro termo da PA: "))
            razao = int(input("Digite a razão da PA: "))
            contador = 0
            PA = 0
        else:
            print("----- Progrma Encerrado -----")
            break
