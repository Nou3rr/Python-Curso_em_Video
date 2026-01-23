#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, a cada 1 b) de 10 até 0, de 2 em 2c) uma contagem personalizada

from time import sleep
def contador(x,y,z):

    if z == 0:
        print(f"{z} é um valor de passo inválido")
        return
    if x < y:
        print("=-" * 15, f"\nContagem de {x} até {y} a cada {z}")
        while x < y:
            print(x, end=" ")
            x = x+z
        if x <= y:
            print(x)
        else:
            print()

    elif x > y:
        print("=-" * 15, f"\nContagem de {x} até {y} a cada {z}")
        z = -z
        while x > y:
            print(x, end=" ")
            x = x+z
        if x >= y:
            print(x)
        else:
            print()
    else:
        print("Contagem inválida, início e fim são iguais.")


contador(0,10,1)
contador(10,0,2)
contador(12,-10,7)
print("=-" * 15, "\nAgora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i,f,p)
print("FIM")
