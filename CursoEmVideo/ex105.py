#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)



def notas(*n,sit=False):
    """
    -> Função para analisar notas e situações de alunos
    :param n: Permite a inserção de diversas notas de alunos para avaliar a situação da turma
    :param sit: se True, mostra a situação da turma conforme a média
    :return: retorna um dicionário com o total de notas, a maior nota, a menor nota, a média e a situação.
    """


    dicionario = dict()
    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n)/len(n)

    if sit:
        if dicionario['media'] < 6:
            dicionario['situação'] = "Ruim"
        elif dicionario['media'] == 6:
            dicionario['situação'] = "Razoável"
        else:
            dicionario['situação'] = "Boa"

    return dicionario
#Programa Principal

resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
help(notas)