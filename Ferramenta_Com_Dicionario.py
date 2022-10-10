from Funcoes_Python.Funcoes_DIC import *

usuarios={}
opcao = perguntar()
while opcao=="I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao=="I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input("Digite o login do que deseja buscar: "))
    if opcao == "E":
        excluir(usuarios, input("Digite o login do que deseja excluir: "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
print("Sistema encerrado!!!")