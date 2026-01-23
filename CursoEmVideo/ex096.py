# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    x = float(input("LARGURA (m): "))
    y = float(input("COMPRIMENTO (m): "))
    total = x*y
    print(f"A área de um terreno de {x}x{y} é de {total}m².")


print("Controle de Terrenos","-"*20)
area()
