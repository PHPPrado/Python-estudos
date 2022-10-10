#Exercício 5.1
x = 1
while x <= 100:
    print(x)
    x = x + 1

#Exercício 5.3
a = 10
while a >= 0:
    print(a)
    a = a - 1
    if a == -1:
        print("Fogo!!!")

#Exercício 5.4
fim = int(input("Digite o último número a imprimir: "))
x = 1
while x <= fim:
    print(x)
    x = x + 2

#Exercício 5.5
x = 0
print("Os 10 primeiros multiplos de 3 são: ")
while x <= 10:
    print(x)
    x = x + 3

#Exercício 5.6
n = int(input("Digite um número para a tabuada: "))
x = 1
while x <= 10:
    print(n * x)
    x = x + 1

#Exercício 5.7
n = int(input("Digite um número para a tabuada: "))
y = int(input("Digite um número para o fim da tabuada: "))
x = 1
while x <= y:
    print(n * x)
    x = x + 1

#Exercício 5.8
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
x = 1
r = 0
while x <= n2:
    r = n1 + r
    x = x + 1
    print(r)

#Exercício 5.9
n1 = int(input("Digite um número para dividir: "))
n2 = int(input("Digite outro número para dividir: "))
r = n1
x = 0

resto = n1 % n2
while (x * n2) <= n1:
    r = r - n2
    x = x + 1
    print(r)
print("Resultado: ", x - 1)
print("Resto: ", resto)

#Exercício 5.10
pontos = 0
questao = 1
while questao <= 3:
    resposta = input("Resposta da questão %d: " % questao).upper()
    if questao == 1 and resposta == "B":
        pontos = pontos + 1
    if questao == 2 and resposta == "A":
        pontos = pontos + 1
    if questao == 3 and resposta == "D":
        pontos = pontos + 1
    questao += 1
print("O aluno fez %d ponto(s)" % pontos)

#Exercício 5.11 e 5.12
saldo = float(input("Digite o valor de depósito inicial: R$"))
juros = int(input("Digite a taxa de juros: "))
juros = juros / 100
c = 1
while c <= 24:
    adicional = float(input("Valor adicional depositado este mês: "))
    saldo = saldo + adicional
    print("Mês ", c,  "%10.2f" % saldo)
    saldo = (saldo + (saldo * juros))
    c += 1

#Exercício5.13
divida = float(input("Digite o valor inicial de uma dívida: "))
juros = int(input("Digite o juros: "))
valor = float(input("Valor mensal a ser pago: "))
mes = 0
total = 0
divida = divida - (valor * (juros/100))
print("Em um mês o valor total da divida cairá para ", divida)
while divida > 0:
    mes = mes + 1
    print(mes, "mes")
    divida = divida - (valor * (juros/100))
    print(divida, "reais")




#Exercício 5.14
b = 0
contador = 0
while True:
    a = int(input("Digite um número ou 0 para sair: "))
    contador = contador + 1
    b = b + a
    if a == 0:
        media = b / contador
        print("A soma de todos os números é: ", b, "\nA média é: ", media)
        break