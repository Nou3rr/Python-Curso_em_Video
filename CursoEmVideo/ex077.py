#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ("eu", "estava", "com", "meus", "mano", "la", "na", "quebrada" )

for palavra in tupla:
    print(f"Na palavra {palavra.upper()}, temos as vogais: ",end="")
    for letra in palavra:
        if letra in "aeiou":
            print(letra,end=" ")
    print()