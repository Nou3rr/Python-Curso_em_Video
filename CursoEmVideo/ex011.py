#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input("Insira a largura da parede em metros: "))
altura = float(input("Insira a altura da parede em metros: "))
area = largura*altura
tinta = area/2

print(f"Sua parede tem {area}m² e você precisará de {tinta} litros de tinta para pintá-la.")
