#Exercício 5.15
p1 = 0.5
p2 = 1.0
p3 = 4.0
p5 = 7.0
p9 = 8.0
total = 0
while True:
    adicionar = input("Deseja adicionar um item a lista? \n Digite 0 para sair! \n Caso queira, digite o nome do produto (P1, P2, P3, P5, P9): \n").lower()
    if adicionar == "p1":
        total = p1 + total
    if adicionar == "p2":
        total = p2 + total
    if adicionar == "p3":
        total = p3 + total
    if adicionar == "p5":
        total = p5 + total
    if adicionar == "p9":
        total = p9 + total
    if adicionar == "0":
        print(total)
        break

#Exercício 5.22
saida = False
while saida == False:
    escolha = input("Escolha uma operação:\n(ADIÇÃO)\n(SUBTRAÇÃO)\n(DIVISÃO)\n(MULTIPLICAÇÃO)\n(SAIR)\nQual operação deseja fazer? ").upper()
    if escolha == "ADIÇÃO":
        numero = int(input("Ótimo, agora digite um número para a tabuada: "))
        x = 0
        while x <= 10:
            valor = numero + x
            x = x + 1
            print(valor)

    if escolha == "SUBTRAÇÃO":
        numero = int(input("Ótimo, agora digite um número para a tabuada: "))
        x = 0
        while x <= 10:
            valor = numero - x
            x = x + 1
            print(valor)

    if escolha == "DIVISÃO":
        numero = int(input("Ótimo, agora digite um número para a tabuada: "))
        x = 0
        while x <= 10:
            valor = numero / x
            x = x + 1
            print(valor)

    if escolha == "MULTIPLICAÇÃO":
        numero = int(input("Ótimo, agora digite um número para a tabuada: "))
        x = 0
        while x <= 10:
            valor = numero * x
            x = x + 1
            print(valor)
    if escolha == "SAIR":
        saida = True

#Exercício 5.23
n = int(input("Digite um número: "))
resto = n % 2
x = 3
while x > n:
    resto = n % x
    x = x + 2
if resto == 0:
    print("O número não é primo.")
else:
    print("Oi primo")

#Exercício 5.25
n = int(input("Digite um número: "))
