#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21

numero = int(input("Digite um número: "))
contador = 0
fibonacci = 0
penultimo = 0

while contador < numero:
    if fibonacci == 0:
        print(fibonacci, end=" ") #valor 0
        fibonacci += 1
        print(fibonacci, end=" ") #valor 1
        contador += 2
    elif fibonacci == 1:
        print(fibonacci, end=" ") #valor 1
        fibonacci += 1
        penultimo = 1
        print(fibonacci, end=" ") #valor 2
        contador += 2
    else:
        fibonacci += penultimo
        penultimo = fibonacci - penultimo
        print(fibonacci, end=" ")
        contador += 1
