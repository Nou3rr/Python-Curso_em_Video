from CursoEmVideo.ex115.lib.interface import *
from CursoEmVideo.ex115.lib.arquivo import *

arquivo = "cursoemvideo.txt"

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(["Ver Pessoas Cadastradas","Cadastrar Nova Pessoa","Sair do Sistema"])
    if resposta == 1:
        #Esta opção lê o conteúdo do arquivo
        lerArquivo('cursoemvideo.txt')

    elif resposta == 2:
        #Esta opção realiza um novo cadastro dentro do arquivo
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaint("Idade: ")
        cadastroArquivo('cursoemvideo.txt',nome,idade)

    elif resposta == 3:
        print("Saindo do sistema, até logo.")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")