#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(x):
    print(x, end="")
    while True:
        x = input().strip()
        if x.isdigit():
            x = int(x)
            break
        else:
            print("ERRO! Digite um número inteiro válido")
    return x

n = leiaint('Digite um número: ')
print(f"Você acabou de digitar o número {n}")