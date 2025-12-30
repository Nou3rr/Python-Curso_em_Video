#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero_a = int(input("Digite o primeiro número: "))
numero_b = int(input("Digite o segundo número: "))
numero_c = int(input("Digite o terceiro número: "))

if numero_a > numero_b and numero_a > numero_c:
    print(f"{numero_a} é o maior número")
    if numero_b > numero_c:
        print(f"{numero_c} é o menor número")
    elif numero_b == numero_c:
        print(f"{numero_b} e {numero_c} são o menor número")
    else:
        print(f"{numero_b} é o menor número")

elif numero_b > numero_a and numero_b > numero_c:
    print(f"{numero_b} é o maior número")
    if numero_a > numero_c:
        print(f"{numero_c} é o menor número")
    elif numero_b == numero_c:
        print(f"{numero_a} e {numero_c} são o menor número")
    else:
        print(f"{numero_a} é o menor número")

elif numero_a < numero_c > numero_b:
    print(f"{numero_c} é o maior número")
    if numero_a > numero_b:
        print(f"{numero_b} é o menor número")
    elif numero_b == numero_a:
        print(f"{numero_b} e {numero_a} são o menor número")
    else:
        print(f"{numero_a} é o menor número")

elif numero_a == numero_b:
    print(f"{numero_a} e {numero_b} são iguais")
    print(f"{numero_c} é o menor número")

elif numero_a == numero_c:
    print(f"{numero_a} e {numero_c} são iguais")
    print(f"{numero_b} é o menor número")

else:
    print(f"{numero_b} e {numero_c} são iguais")
    print(f"{numero_a} é o menor número")
