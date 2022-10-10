# Capítulo 6 - Listas

# Exercício 6.1 - Média

# notas = [0,0,0,0,0,0,0,]
# media = 0
# cont = 0

# Ler notas------------------------------
# while cont < 7 :
#     notas[cont] = float(input("Digite a nota da prova %d : " % cont))
#     media = media + notas[cont]
#     cont += 1

# Imprimir as notas----------------------
# cont = 0
# while cont < len(notas) :
#     print("A prova ", cont, " recebeu nota ", notas[cont])
#     cont += 1
# media = media/7
# print("A média das notas é de %2.1f" % media)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# Exercício 6.2 e 6.3
#
# lista1 = []
# cont = 0
# limite = int(input("Digite o tamanho das listas: "))
# while cont < limite :
#     n = int(input("Digite o %d° valor: " % cont))
#     lista1.append(n)
#     cont += 1
# print(lista1)
# lista2 = []
# cont = 0
# while cont < limite:
#     n = int(input("Digite o %d valor: " % cont))
#     lista2.append(n)
#     cont += 1
# print(lista2)
#
# cont1 = 0
# cont2 = 0
# while cont1 < len(lista1):
#     while cont2 < len(lista2):
#         if lista1[cont1] == lista2[cont2]:
#             del lista2[cont2]
#         cont2 += 1
#     cont1 += 1
#     cont2 = 0
#
# lista1.extend(lista2)
# print(lista1)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.5 e 6.6
#
# ultimo = 10
# fila = list(range(1, ultimo, +1))
# ultimo2 = 10
# fila2 = list(range(1, ultimo2, +1))
# while True:
#     print("\nExistem %d clientes na fila" % len(fila))
#     print("Fila atual:", fila)
#     print("Fila atual:", fila2)
#     print("Digite F para adicionar um cliente ao fim da fila,")
#     print("ou A para realizar o atendimento. S para sair.")
#     cont = 0
#     operacao = []
#     while cont < len(fila) or cont < len(fila2):
#         operacao.append(input("Operação (F, A ou S):").upper())
#         cont += 1
#         print(operacao)
#     cont = -2
#     while cont < len(fila) or cont < len(fila2):
#         if operacao[cont] == "A":
#             if(len(fila)) > 0:
#                 atendido = fila.pop(0)
#                 print("Cliente %d atendido" % atendido)
#             else:
#                 print("Fila vazia! Ninguém para atender.")
#         elif operacao[cont] == "B":
#             if(len(fila2)) > 0:
#                 atendido = fila2.pop(0)
#                 print("Cliente %d atendido" % atendido)
#             else:
#                 print("Fila vazia! Ninguém para atender.")
#         elif operacao[cont] == "F":
#             ultimo += 1
#             fila.append(ultimo)
#         elif operacao[cont] == "G":
#             ultimo2 += 1
#             fila2.append(ultimo2)
#         elif operacao[cont] == "S":
#             break
#         else:
#             print("Operação inválida! Digite apenas F, A ou S!")
#         cont += 1

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.7

# expressao = input("Digite uma expressão de parênteses: ")
# cont = 0
# abre = []
# fecha = []
# while cont < len(expressao):
#     if expressao[cont] == "(":
#         abre.append('(')
#     elif expressao[cont] == ")":
#         fecha.append(')')
#     cont += 1
# if len(abre) == len(fecha):
#     print("OK")
# else:
#     print("Erro")
# abre.extend(fecha)
# print(abre)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.8, 6.9 e 6.10

# L=[15,7,27,39]
# p=int(input("Digite o valor a procurar: "))
# x=0
# # checkp = False
# # checkv = False
# while x < len(L):
#     if L[x]==p:
#         print("%d achado na posição %d" % (p, x))
#         break
#     x += 1
# if x >= len(L):
#     print("Não encontrado")
# v=int(input("Digite o valor a procurar: "))
# x=0
# while x < len(L):
#     if L[x]==v:
#         print("%d achado na posição %d" % (v, x))
#         checkv = True
#     x += 1
# if checkv == False:
#     print("%d não encontrado" % v)
#
# if (checkp == True and checkv == True) or (checkp == True and checkv == False):
#     print("O valor p foi encontrado primeiro")
# elif checkp == False and checkv == True:
#     print("O valor v foi encontrado primeiro")
# else:
#     print("Nenhum valor foi encontrado.")

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Enumerate in for

# L=[5,9,13]
# for x, e in enumerate(L):
#     print("[%d] %d" % (x,e))

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.13

# t = [-10, -8, 0, 1, 2, 5, -2, -4]
# print(max(t))
# print(min(t))
# print(sum(t)/len(t))

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# lugares_vagos=[10,2,1,3,0]
# while True:
#     sala=int(input("Sala (0 sai): "))
#     if sala == 0:
#         print("Fim")
#         break
#     if sala>len(lugares_vagos) or sala<1:
#         print("Sala inválida")
#     elif lugares_vagos[sala-1]==0:
#         print("Desculpe, sala lotada!")
#     else:
#         lugares =int(input("Quantos lugares você deseja (%d vagos):"
#         % lugares_vagos[sala-1]))
#     if lugares > lugares_vagos[sala-1]:
#         print("Esse número de lugares não está disponível.")
#     elif lugares < 0:
#         print("Número inválido")
#     else:
#         lugares_vagos[sala-1]-=lugares
#         print("%d lugares vendidos" % lugares)
# print("Utilização das salas")
# for x,l in enumerate(lugares_vagos):
#     print("Sala %d - %d lugar(es) vazio(s)" % (x+1, l))

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# L=[1,2,3,4,5]
# fim=5
# while fim > 1:
#     trocou=False
#     x=0
#     while x<(fim-1):
#          if L[x] < L[x+1]:
#             trocou=True
#             temp=L[x]
#             L[x]=L[x+1]
#             L[x+1]=temp
#          x+=1
#     if not trocou:
#         break
#         fim-=1
# for e in L:
#     print(e)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Dicionários---------
# tabela = { "Alface": 0.45,
#  "Batata": 1.20,
#  "Tomate": 2.30,
#  "Feijão": 1.50 }
# while True:
#     produto=input("Digite o nome do produto, fim para terminar:")
#     if produto == "fim":
#         break
#     if produto in tabela:
#         print("Preço %5.2f" % tabela[produto])
#     else:
#         print("Produto não encontrado!")

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.17
# estoque={ "tomate": [ 1000, 2.30],
#  "alface": [ 500, 0.45],
#  "batata": [ 2001, 1.20],
#  "feijão": [ 100, 1.50] }
#
# venda = []
# resultado = []
# while True:
#     # for dado in estoque:
#         produto = input("Digite o nome do produto: ")
#         if produto in estoque:
#             quantidade = int(input("Digite a quantidade vendida: "))
#             resultado.append(produto)
#             resultado.append(quantidade)
#             venda.append(resultado)
#             resultado = []
#             estoque[produto][0] -= quantidade
#         continuar = input("Deseja adicionar mais informações? : ").upper()
#         if continuar != "SIM":
#             break
# print(venda)
# print(estoque)
# total = 0
#
# print("Vendas:\n")
# for operação in venda:
#     produto = operação[0]
#     quantidade = operação[1]
#     preço = estoque[produto][1]
#     custo = preço * quantidade
#     print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade,preço,custo))
#     estoque[produto][0] -= quantidade
#     total+=custo
# print(" Custo total: %21.2f\n" % total)
# print("Estoque:\n")
# for chave, dados in estoque.items():
#     print("Descrição: ", chave)
#     print("Quantidade: ", dados[0])
#     print("Preço: %6.2f\n" % dados[1])

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

#Exercício 6.18

# frase = input("Escreva alguma coisa: ")
# dic = {}
# cont = 0
# for l in frase:
#     l = frase[cont]
#     if l in dic:
#         dic[frase[cont]] += 1
#     else:
#         dic[frase[cont]]= 1
#     cont += 1
# print(dic)

#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

