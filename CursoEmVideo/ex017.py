#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
from math import sqrt

cateto_oposto = float(input("Insira o cateto oposto: "))
cateto_adjascente = float(input("Insira o cateto adjascente: "))
hipotenusa = sqrt(cateto_oposto**2 + cateto_adjascente**2)

print(f"A hipotenusa tem o valor de {hipotenusa}")