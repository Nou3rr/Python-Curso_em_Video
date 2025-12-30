#Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar [ 2 ] multiplicar [ 3 ] maior [ 4 ] novos números
# [ 5 ] sair do programa Seu programa deverá realizar a operação solicitada em cada caso

numero_a = int(input("Digite um valor: "))
numero_b = int(input("Digite outro valor: "))

while True:
    menu = int(input("----- CALCULADORA -----\n[1] Soma\n[2] Multiplicação\n[3] Maior\n[4] Novos Números\n[5] Encerrar programa\n"))
    if menu == 1:
        print(numero_a+numero_b)
    elif menu == 2:
        print(numero_a*numero_b)
    elif menu == 3:
        if numero_a >= numero_b:
            print(f"O maior número é {numero_a}")
        else:
            print(f"O maior número é {numero_b}")
    elif menu == 4:
        numero_a = int(input("Digite um valor: "))
        numero_b = int(input("Digite outro valor: "))
    elif menu == 5:
        print("----- Encerrando Programa -----")
        break
    else:
        print("Erro! Entrada inválida")