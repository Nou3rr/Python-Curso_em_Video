#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média

pessoas = []
pessoa={}
soma_idade = 0

while True:
    pessoa['nome'] = input("Nome: ")
    while True:
        pessoa['sexo'] = input("Sexo: [M/F] ").lower().strip()
        if pessoa['sexo'] not in "mf":
            print("ERRO! Por favor, digite apenas M ou F.")
        else:
            break
    pessoa['idade'] = int(input("Idade: "))
    soma_idade += pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        continuar = str(input("Deseja continuar? [S/N] ")).lower().strip()
        if continuar not in "sn":
            print("ERRO! Por favor, digite apenas S ou N.")
        else:
            break
    if continuar == "n":
        break
media_idade = soma_idade/len(pessoas)

print("-="*30)
print(f"A) Ao todo temos {len(pessoas)} cadastradas.")
print(f"B) A média de idade é {media_idade:.2f} anos.")
print(f"C) As mulheres cadastradas foram ",end="")
for dicionario in pessoas:
    if dicionario['sexo'] == "f":
        print(dicionario['nome'],end=" ")
print(f"\nD) Lista de pessoas com idade acima da média:")
for dicionario in pessoas:
    if dicionario['idade'] > media_idade:
        print(dicionario)
