#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

medida_a = int(input("Digite a primeira medida do triângulo: "))
medida_b = int(input("Digite a segunda medida do triângulo: "))
medida_c = int(input("Digite a terceira medida do triângulo: "))

if medida_a+medida_b > medida_c and medida_a+medida_c > medida_b and medida_b+medida_c > medida_a:
    print("Um triângulo pode ser formado")
else:
    print("Um triângulo não pode ser formado")