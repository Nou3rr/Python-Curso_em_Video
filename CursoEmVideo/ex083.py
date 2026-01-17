#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expression = input("Digite uma expressão: ").strip().lower()
pilha = []

for item in expression:
    if item == "(":
        pilha.append(item)
    elif item == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break

if len(pilha) > 0:
    print(f"A expressão é inválida")
else:
    print(f"A expressão é válida")