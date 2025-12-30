#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, cos, sin, tan

angulo = float(input("Insira um ângulo: "))
rad = radians(angulo)

seno = sin(rad)
cosseno = cos(rad)
tan = tan(rad)

print(f"O ângulo inserido foi {angulo}º\nSeu seno é {seno:.2f}\nSeu cosseno é {cosseno:.2f}\nSua tangente é {tan:.2f}")