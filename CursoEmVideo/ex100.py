#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(lista):
    for i in range(0,5):
        lista.append(randint(0,10))
    print(lista)

def somapar(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    print(soma)

numeros = []
sorteia(numeros)
somapar(numeros)