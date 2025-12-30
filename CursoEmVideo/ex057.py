#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    genero = input("Insira seu gênero [M/F]: ").lower().strip()
    if genero == "m":
        print("Genêro masculino!")
        break
    elif genero == "f":
        print("Gênero feminino!")
        break
    else:
        print("Entrada de gênero inválida! Insira apenas M ou F.")