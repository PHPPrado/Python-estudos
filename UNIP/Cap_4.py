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
