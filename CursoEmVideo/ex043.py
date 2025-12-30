#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso– Entre 18,5 e 25: Peso Ideal– 25 até 30: Sobrepeso– 30 até 40: Obesidade– Acima de 40: Obesidade Mórbida

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em quilos: "))
imc = peso/(altura**2)

if imc < 18.5:
    print(f"IMC {imc}: Desnutrição")
elif 18.4 < imc < 25:
    print(f"IMC {imc}: Peso ideal")
elif 24.9 < imc < 30:
    print(f"IMC {imc}: Sobrepeso")
elif 29.9 < imc < 40:
    print(f"IMC {imc}: Obesidade")
else:
    print(f"IMC {imc}: Obesidade mórbida")
