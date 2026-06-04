from CursoEmVideo.ex115.lib.interface import *

def arquivoExiste(nome): #Esta função verifica a existência de um arquivo, tentando abri-lo.
    try:
        a = open(nome, 'rt') #Tenta abrir o arquivo para ler r- read, t- text
        a.close() #Fecha o arquivo

    except FileNotFoundError: #Caso o arquivo não exista, retorna o valor Falso
        return False
    else: #Caso o arquivo exista, retorna verdadeiro
        return True

def criarArquivo(nome): #Esta função verifica a existência de um arquivo, e se necessário cria um arquivo.
    try:
        a = open(nome, 'wt+') #essa linha tenta abrir o arquivo e escrever, w = write, t = text, + = cria um arquivo caso ainda não exista
        a.close()
    except:
        print("Houve um erro na criação do arquivo!")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def lerArquivo(nome): #Esta função lê o arquivo e exibe seu conteúdo na tela para o usuário
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('\033[031mErro ao ler o arquivo!\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30} {dado[1]:>3} anos")
    finally:
        a.close()

def cadastroArquivo(arquivo, nome = 'desconhecido', idade = 0): #Esta função realiza novos cadastros no arquivo
    try:
        a = open(arquivo, 'at')
    except:
        print("\033[031mHouve um erro na abertura do arquivo!\033[m")
    else:
        try:
            a.write(f"{nome};{idade}\n")
        except:
            print("\033[031Houve um erro na escrita de dados\033[m")
        else:
            print(f"{nome} foi adicionado ao registro")
            a.close()
