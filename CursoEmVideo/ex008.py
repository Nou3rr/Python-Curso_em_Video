#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input("Digite a medida em metros para ser convertida: "))
centimetros = metros*100
milimetros = metros*1000

print(f"{metros}m convertido para centímetros é {centimetros:.2f}cm e convertido para milímetros é {milimetros:.2f}mm")