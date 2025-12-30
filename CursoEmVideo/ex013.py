#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salário atual: "))
aumento = salario*1.15

print(f"O novo salário com aumento de 15% é R$ {aumento:.2f}")