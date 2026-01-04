#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    contador = 1
    numero = int(input("Quer ver a tabuada de qual valor? [0 para sair]: "))
    if numero != 0:
        while contador < 11:
            print(f"{contador} x {numero} = {contador*numero}")
            contador += 1
    else:
        break
