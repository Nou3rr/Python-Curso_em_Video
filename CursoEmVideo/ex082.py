#Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numbers = list()
even = list()
odd = list()

while True:
    numbers.append(int(input("Digite um número: ")))
    if numbers[-1] % 2 == 0:
        even.append(numbers[-1])
    else:
        odd.append(numbers[-1])
    continuar = input("Deseja continuar? [S/N]: ").lower().strip()
    if continuar != "s":
        break

print(f"Os números inseridos foram: {numbers}")
print(f"Os números pares inseridos foram: {even}")
print(f"Os números ímpares inseridos foram: {odd}")