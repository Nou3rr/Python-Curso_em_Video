#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

adultos = 0
homens = 0
mulheres_menos_20 = 0

while True:
    cadastrar = input("Digite [s] para cadastrar uma pessoa ou qualquer outra tecla para encerrar o programa\n").lower().strip()
    if cadastrar == "s":

        sexo = input("Digite [m] para sexo masculino ou [f] para sexo feminino: ").lower().strip()
        if sexo == "m":
            idade = int(input("Digite a idade: "))
            if idade > 18:
                adultos += 1
                homens += 1
            else:
                homens += 1

        elif sexo == "f":
            idade = int(input("Digite a idade: "))
            if idade < 20:
                mulheres_menos_20 += 1

    else:
        print("----- Programa Encerrado -----")
        print(f"Foram cadastrados {adultos} homens com mais de 18 anos")
        print(f"Foram cadastrados {homens} de qualquer idade")
        print(f"Foram cadastradas {mulheres_menos_20} com menos de 20 anos")
        break