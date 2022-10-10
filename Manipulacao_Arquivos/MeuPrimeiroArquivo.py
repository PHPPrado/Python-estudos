#Com a abertura deste arquivo que eu apelidei de "arquivo", faça:
#escrever no arquivo "hakuna matata"

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.readline()
    for linha in arquivo.readlines():
        print(linha)
