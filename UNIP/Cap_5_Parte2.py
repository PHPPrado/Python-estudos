"""
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
"""
# Exercício 5.23
# n = int(input("Digite um número: "))
# resto = n % 2
# x = 3
# -----Excessões-----
# if (n == 2) or (n == 1):
#     print("Oi primo", n)
#     exit()
# while x > n:
#     resto = n % x
#     x = x + 2
# if resto == 0:
#     print("O número não é primo.")
# else:
#     print("Oi primo", n)

# Exercício 5.24
# quantidade = int(input("Quantos números primos deseja imprimir?"))
#
#
# armazenamento = 0
# contador = 0
#
# inicio = 2
# numero = 2
#
# while contador <= quantidade:
#     while inicio < numero:
#         calculo = numero % inicio
#         inicio += 1
#         if calculo == 0:
#             armazenamento += 1
#
#     if armazenamento == 0:
#         print(numero)
#         contador += 1
#
#     numero += 1
#     inicio = 2
#     armazenamento = 0
#


"""
#Exercício 5.25
n = int(input("Digite um número: "))
p = (2+(n/2))/2
print(p)

#Exercício 5.26
numero = int(input("Digite um número: "))
numero2 = int(input("Agora digite seu divisor: "))

numero_irmao = numero
contador = 0
while numero >= numero2:
    numero_irmao = numero_irmao - numero2
    contador = contador + 1
    print(numero_irmao)

"""
#Exercício 5.27
# n = input("Digite um número: ")
# c = len(n) - 1
# while c < len(n):
#     i1 = n[c]
#     print(i1)
#     c += 1
#
# n1 = float(input("Digite um numero: "))
# n2 = float(input("Digite um numero: "))
# r = 0
# x = n1
# while x > 0:
#     x = x - n2
#     print(x)
#     r = r + 1
# print(r)

# n1 = int(input("Digite um numero: "))
# n2 = int(input("Digite um numero: "))
# r = 0
# cont = 1
# while cont < n2 :
#     r = r + n2
#     cont += 1
# print(r)

# pdia = int(input("Digite quantos por dia: "))
# jfumou  = int(input("Digite quantos já fumou: "))
# total = (jfumou * 10) + (pdia * 10)
# total = total / 1440
# print(round(total), " dias")

