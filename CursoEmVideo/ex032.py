#Faça um programa que leia um ano qualquer e mostre se ele é bissexto

ano = int(input("Digite um ano para saber se ele é bissexto: "))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f"{ano} é um ano bissexto, porque é divisível por 400 ")
        else:
            print(f"Não é um ano bissexto, porque é divisível por 100 mas não por 400")
    else:
        print(f"{ano} é um ano bissexto, porque é divisível por 4 mas não por 100")
else:
    print(f"{ano} não é um ano bissexto, porque não é divisível por 4")