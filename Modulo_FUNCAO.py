from Funcoes_Python.Definindo_FUNCOES import *

minhaLista=[]
print("Preenchendo...")
preencherInventario(minhaLista)
print("Exibindo...")
exibirInventario(minhaLista)

print("Pesquisando...")
localizarPorNome(minhaLista)
print("Alterando...")
depreciarPorNome(minhaLista, 20)

print("Excluindo.........feito!")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)
print("Common JSON")