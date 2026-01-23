#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto):
    tamanho = len(texto)+4
    print(f"~"*tamanho)
    print(f"{texto:^{tamanho}}")
    print(f"~" * tamanho)

escreva("Kauan")
escreva("Curso em Vídeo")
