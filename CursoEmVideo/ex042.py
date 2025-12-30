#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes


medida_a = int(input("Digite a primeira medida do triângulo: "))
medida_b = int(input("Digite a segunda medida do triângulo: "))
medida_c = int(input("Digite a terceira medida do triângulo: "))

if medida_a+medida_b > medida_c and medida_a+medida_c > medida_b and medida_b+medida_c > medida_a:
    print("Um triângulo pode ser formado")
    tipo = int(input("Insira [1] para saber o tipo de triangulo, ou qualquer outro número para sair:\n"))
    if tipo == 1:
        if medida_a == medida_b == medida_c:
            print("Triângulo EQUILÁTERO")
        elif medida_a == medida_b or medida_a == medida_c or medida_b == medida_c:
            print("Triângulo ISÓSCELES")
        elif medida_a != medida_b != medida_c:
            print("Triângulo ESCALENO")
else:
    print("Um triângulo não pode ser formado")

