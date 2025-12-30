#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius para converte-la para Fahrenheit: "))
fahrenreit = celsius * 1.8 + 32

print(f"{celsius}ºC em Fahrenreit é {fahrenreit}ºF")