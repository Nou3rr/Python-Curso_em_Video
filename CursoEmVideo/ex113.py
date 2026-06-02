#Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(x):
    while True:
        try:
            n = int(input(x))

        except (ValueError, TypeError):
            print("ERRO! Por favor, digite um número inteiro válido.")

        except (KeyboardInterrupt):
            print("ERRO! O usuário optou em não inserir um número. A variável receberá o valor 0.")
            n = 0
            return n

        else:
            return n



def leiafloat(y):
    while True:
        try:
            n = float(input(y))

        except (ValueError, TypeError):
            print("ERRO! Por favor, digite um número decimal inteiro válido.")

        except (KeyboardInterrupt):
            print("ERRO! O usuário optou em não inserir um número. A variável receberá o valor 0.")
            n = 0
            return n

        else:
            return n


n1 = leiaint('Digite um número inteiro: ')
n2 = leiafloat('Digite um número decimal: ')
print(f"Você acabou de digitar o número {n1} e {n2}")
