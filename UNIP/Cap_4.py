"""

#Exercício 4.2
velocidade = int(input("Qual a velocidade do veículo? "))
if velocidade > 80:
    print("Você foi multado(a).")
    diferenca = velocidade - 80
    print("Você deve pagar", 5 * diferenca, "reais")

#Exercício 4.3
a = int(input("Digite um número: "))
b = int(input("Digite mais um número: "))
c = int(input("Digite só mais um número: "))
if a > b and a > c:
    print(a, "é o maior.")
elif b > a and b > c:
    print(b, "é o maior.")
elif c > b and c > a:
    print(c, "é o maior.")

if a < b and a < c:
    print(a, "é o menor.")
elif b < a and b < c:
    print(b, "é o menor.")
elif c < b and c < a:
    print(c, "é o menor.")


#Exercício 4.4
salario = float(input("Digite seu salário: "))
if salario > 1250.00:
    salario = salario + (salario * 0.1)
else:
    salario = salario + (salario * 0.15)
print("R$", salario)

#Exercício 4.6
dist = int(input("Digite a distância percorrida: "))
if dist <= 200:
    print("O valor da passagem é de ", 0.5 * dist, "reais")
else:
    print("O valor da passagem é de ", 0.45 * dist, "reais")

#Exercício 4.9
valor = int(input("Qual o valor da casa: "))
salario = int(input("Digite o salario: "))
anos = int(input("Digite a quantidade de anos: "))
prest = valor / (12 * anos)
if prest > (0.3 * salario):
    print("Você não conseguirá pagar esta casa!")
else:
    print(prest)
"""
#Exercício 4.10
# kwh = int(input("Digite a quantidade consumida: "))
# tipo=input("Digite o tipo de instalação: ").upper()
# if tipo == "R":
#     if kwh <= 500:
#      kwh = kwh * 0.4
#     else:
#         kwh = kwh * 0.65
# if tipo =="C":
#     if kwh <= 1000:
#      kwh = kwh * 0.55
#     else:
#         kwh = kwh * 0.60
# if tipo =="I":
#     if kwh <= 5000:
#      kwh = kwh * 0.55
#     else:
#         kwh = kwh * 0.60
# print(kwh)
