#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()

for i in range(0,5):
    numero = int(input("Digite um número: "))
    if numero in lista:
        print("Este número já foi adicionado")
    else:
        lista.append(numero)
print(sorted(lista))