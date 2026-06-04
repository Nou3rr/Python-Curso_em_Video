def leiaint(x):
    while True: #Esta função garante que o usuário insira uma entrada válida, e caso haja interrupção, a função entrega uma variável com um valor que encerra o programa.
        try:
            n = int(input(x))

        except (ValueError, TypeError):
            print("\033[31mERRO! Por favor, digite um número inteiro válido.\033[m")

        except KeyboardInterrupt:
            print("\033[31mERRO! O usuário optou em não inserir um número. O programa será encerrado.\033[m")
            return 3

        else:
            return n


def linha(tam = 42): #Esta função cria linhas de 42 traços
    return "-" * tam


def cabecalho(txt): #Esta função cria um cabeçalho centralizado
    print(linha())
    print(txt.center(len(linha()))) #Fazer dessa forma, permite que titulo seja centralizado sempre levando em consideração o tamanho informado na função linha
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL") #Esta função cria um menu em forma de lista, com alguns detalhamentos coloridos.
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaint("Sua opção: ")
    return opc




