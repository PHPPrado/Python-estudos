# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
# maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
# precisa que você faça um programa que leia a variável peso (peso de peixes)
# e calcule o excesso. Gravar na variável excesso a quantidade de quilos além
# do limite e na variável multa o valor da multa que João deverá pagar. Imprima
# os dados do programa com as mensagens adequadas.



# quilos = float(input("Olá João, quantos peixes temos hoje? "))
# taxa = 4.00
# limite = 50
# if quilos > limite:
#     multa = (quilos - limite) * taxa
#     print("Este valor está acima do limite de ", limite, " quilos.\nUma multa será cobrada no valor de R$", multa)
# else:
#     print("O valor limite de ", limite, " quilos, não foi ultrapassado. Tenha um bom dia :)")

#------------------------------------------------------------------------------------------------------------------------

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
# a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
# latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# Comprar apenas latas de 18 litros;
# Comprar apenas galões de 3,6 litros;
# Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
# arredonde os valores para cima, isto é, considere latas cheias.

# tamanho = float(input("Digite o tamanho em metros da área a ser pintada: "))
#
# if tamanho > 108:
#     print("Compre latas de 18 litros.")
# else:
#     print("Compre ", tamanho/22, " galões de tinta.")

#------------------------------------------------------------------------------------------------------------------------

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo.
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

# numero1 = int(input("Digite um número: "))
# numero2 = int(input("Digite outro número: "))
# numero3 = float(input("Digite agora um número real: "))
# conta1 = (2 * numero1) * (numero2 / 2)
# conta2 = (3 * numero1) + numero3
# conta3 = numero3 ** 3
# print("O produto do dobro do primeiro com a metade do segundo é ", conta1)
# print("A soma do triplo do primeiro com o terceiro é de ", conta2)
# print("O terceiro elevado ao cubo é %2.2f" % conta3)

#------------------------------------------------------------------------------------------------------------------------

# Faça um programa que leia três valores inseridos pelo usuário e calcula
# as raízes da equação de Bhaskara. Caso não seja possível calcular as
# raízes, imprima uma mensagem ao usuário, informando-o que não é possível
# executar o cálculo. Considere que o usuário irá inserir os valores na
# seguinte ordem: a, b e c (ax² + bx + c).


# a = int(input("Digite o valor de (a): "))
# b = int(input("Digite o valor de (b): "))
# c = int(input("Digite o valor de (c): "))
# delta = b**2 - 4 * a * c
# print("Delta vale ", delta)
# if delta < 0:
#     print("Não é possível continuar.")
#     exit()
# raiz = delta ** (1/2) #Cálculo da raiz quadrada!
# x1 = (-b + raiz) / 2 * a
# x2 = (-b - raiz) / 2 * a
#
# print("Os valores possíveis de x são ", x1, " e ", x2)

#------------------------------------------------------------------------------------------------------------------------

# Faça um programa que identifique o local no plano (eixo cartesiano com duas dimensões)
# em que se encontra um ponto inserido pelo usuário (primeira linha corresponde ao
# valor de x no par ordenado, a segunda linha corresponde ao valor de y). Caso o ponto
# esteja na origem, imprima na tela a mensagem 'O ponto se encontra na origem', se o
# ponto estiver sobre um dos eixos imprima a mensagem
# 'O ponto se encontra sobre o eixo X', ou 'O ponto se encontra sobre o eixo Y'
# dependendo da situação, caso nenhuma das situações descritas anteriormente descreva
# a posição do ponto, informe o quadrante em que ele se encontra.

# x = int(input("Digite o valor de x: "))
# y = int(input("Digite o valor de y: "))
#
# if x > 0 and y > 0:
#     print("Estão no primeiro quadrante.")
# elif x > 0 and y < 0:
#     print("Estão no quarto quadrante.")
# if y > 0 and x < 0:
#     print("Estão no segundo quadrante.")
# elif x < 0 and y < 0:
#     print("Estão no terceiro quadrante.")
# if x == 0 and y == 0:
#     print("Estão no ponto 0")

#------------------------------------------------------------------------------------------------------------------------

# Faça um programa que calcule a média de diversos números inseridos pelo usuário.
# Para isso, crie uma função que recebe como parâmetro a quantidade de notas que
# serão inseridas e retorne a média, com duas casas decimais, para quem a invocou.
# Receba a quantidade de notas do usuário e depois receba cada nota até chegar na quantidade solicitada.
# m = 0
# y = 1
# saida = "SIM"
# while saida != "NÃO" or saida != "NAO":
#     x = int(input("Digite um número: "))
#     saida = input("Deseja sair? ")
#     m = m + x
#     y = y + 1
# print(m / y)

#------------------------------------------------------------------------------------------------------------------------

# numero1 = int(input("Digite um numero: "))
# numero2 = int(input("Digite um numero: "))
# operacao = input("Digite a operação: ")
# if operacao == "+":
#     print(numero1 + numero2)
# elif operacao == "-":
#     print(numero1 - numero2)
# else:
#     if operacao == "*":
#         print(numero1 * numero2)
#     elif operacao == "/":
#         print(numero1 / numero2)
#     else:
#         print("Operação invalida")
#
#------------------------------------------------------------------------------------------------------------------------

# valor = float(input("Digite o valor do imovel: "))
# salario = float(input("Digite o seu salário: "))
# anos = int(input("Digite quantos anos: "))
#
# if (valor/anos) < (salario * 0.3):
#     print(valor/anos)
# else:
#     print("Prestações acima do teto.")

#------------------------------------------------------------------------------------------------------------------------
#
# saque = int(input("Digite o quanto quer sacar: "))
# ced200 = 0
# ced100 = 0
# ced50 = 0
# ced20 = 0
# ced10 = 0
# ced5 = 0
# ced2 = 0
# ced1 = 0
# while True:
#     if saque >= 200:
#         saque = saque - 200
#         ced200 = ced200 + 1
#     elif (saque < 200) and (saque >= 100):
#         saque = saque - 100
#         ced100 = ced100 + 1
#     if (saque < 100) and (saque >= 50):
#         saque = saque - 50
#         ced50 = ced50 + 1
#     elif (saque < 50) and (saque >= 20):
#         saque = saque - 20
#         ced20 = ced20 + 1
#     if (saque < 20) and (saque >= 10):
#         saque = saque - 10
#         ced10 = ced10 + 1
#     elif (saque < 10) and (saque >= 5):
#         saque = saque - 5
#         ced5 = ced5 + 1
#     if (saque < 5) and (saque >= 2):
#         saque = saque - 2
#         ced2 = ced2 + 1
#     elif (saque < 2) and (saque >= 1):
#         saque = saque - 1
#         ced1 = ced1 + 1
#     if saque == 0:
#         break
# print("200 -> ", ced200)
# print("100 -> ",ced100)
# print("50 -> ",ced50)
# print("20 -> ",ced20)
# print("10 -> ",ced10)
# print("5 -> ",ced5)
# print("2 -> ",ced2)
# print("1 -> ",ced1)

#------------------------------------------------------------------------------------------------------------------------
#
# Utilizando listas faça um programa que faça 5 perguntas para uma
# pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a
# participação da pessoa no crime. Se a pessoa responder positivamente
# a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
# como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será
# classificado como "Inocente".

#------------------------------------------------------------------------------------------------------------------------


# questionario = {
#     "Telefonou para a vítima?":[False],
#     "Esteve no local do crime?":[False],
#     "Mora perto da vítima?":[False],
#     "Devia para a vítima?":[False],
#     "Já trabalhou com a vítima?":[False]
# }
#
# cont = 1
# for pergunta in questionario:
#     resposta = input("Resposta da %d pergunta: " %cont).upper()
#     if resposta == "SIM":
#         questionario[pergunta][0] = True
#         cont += 1
    # resposta = input("Esteve no local do crime?").upper()
    # if resposta == "SIM":
    #     questionario[pergunta][0] = True
    #     continue
    # resposta = input("Mora perto da vítima?").upper()
    # if resposta == "SIM":
    #     questionario[pergunta][0] = True
    #     continue
    # resposta = input("Devia para a vítima?").upper()
    # if resposta == "SIM":
    #     questionario[pergunta][0] = True
    #     continue
    # resposta = input("Já trabalhou com a vítima?").upper()
    # if resposta == "SIM":
    #     questionario[pergunta][0] = True
    #     continue


# contagem = 0
# for pergunta in questionario:
#     if questionario[pergunta][0] == True:
#         contagem += 1
#
# print(questionario)
# print(contagem)
#
# if contagem == 2:
#     print("Suspeita")
# elif contagem >= 3 <= 4:
#     print("Cúmplice")
# elif contagem == 5:
#     print("Assassino")
# else:
#     print("Liberado")

#------------------------------------------------------------------------------------------------------------------------

# Escreva uma função, chamada contaVoigais, que conta todas
# as vogais presentes no texto recebido como parâmetro e
# retorna um dicionário contendo a quantidade de cada vogal.
# Escreva um programa a fim de testar sua função, e exiba, no
# fim, os dados do dicionário retornado.

# def contaVogais(texto):
# #     vogais = {"A": [0], "E": [0], "I": [0], "O": [0], "U": [0]}
# #     texto.upper()
# #     str(texto)
# #     for letra in texto:
# #         print(letra)
# #         if letra in vogais:
# #             vogais[letra][0] += 1
# #     return vogais
# #
# # print(contaVogais("POPOCAS"))

#------------------------------------------------------------------------------------------------------------------------

# https://www.respondeai.com.br/conteudo/programacao/python/lista-de-exercicios/tuplas-e-dicionarios-2182

#Exercício 2

agenda = {}
chave = 0
resposta = 1
x = 0

while resposta != 0:

    def incluirNovoNome():
        nome = input("Digite o novo nome: ")
        agenda[nome] = ''
    def incluirTelefone():
        nome = input("Digite o nome de quem quer adicionar um número: ")
        if nome in agenda:
            agenda[nome][x] += input("Digite o número a ser adicionado: ")
        else:
            print("Nome não encontrado :( ")
            incluirNovoNome()

    print(agenda)

    resposta = int(input("Bem vindo(a) ao registro telefonico, o que deseja fazer?"
                         "\nIncluir novo nome.........[1]"
                         "\nIncluir telefone..........[2]"
                         "\nExcluir telefone..........[3]"
                         "\nExcluir nome..............[4]"
                         "\nConsultar telefone........[5]"
                         "\nSair......................[0]"
                         "\nDigite sua resposta: "))
    if resposta == 1:
        incluirNovoNome()
        continue

    elif resposta == 2:
        incluirTelefone()
        continue

    elif resposta == 3:
        nome = input("Digite o nome de quem quer excluir um número: ")
        if nome in agenda:
            agenda[nome][x] -= input("Digite o número a ser excluir: ")
            continue