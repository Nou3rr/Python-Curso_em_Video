#Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(numero,show=False):
    f = 1
    for i in range(numero,0,-1):
        f *= i
        if show:
            if i > 1:
                print(f"{i} x ",end="")
            else:
                print(f"{i} = ", end="")
                return f
        else:
            return f

print(fatorial(5,show=False))
print(fatorial(6,show=True))
