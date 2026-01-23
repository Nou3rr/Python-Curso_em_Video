#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep

def maior(*n):
    print("=-" * 20, "\nAnalisando os valores passados...")
    sleep(0.3)
    if len(n) == 0:
        print(f"Nenhum número foi informado.")
    else:
        for numero in n:
            print(numero, end=" ")
            sleep(0.3)
        print(f"\nForam informados {len(n)} valores ao todo")
        sleep(0.3)
        print(f"O maior valor informado foi {max(n)}")

maior(2,9,4,5,7,1)
maior()