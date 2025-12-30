#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input("Digite o salário para saber seu aumento: "))
if salario > 1250:
    print(f"Você receberá um aumento de 10%, seu novo salário é R$ {salario*1.1:.2f}")
else:
    print(f"Você receberá um aumento de 15%, seu novo salário é R$ {salario*1.15:.2f}")