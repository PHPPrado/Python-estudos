inventario = []
resposta = "S"
while resposta == "S":
#inventario.append = inserir no inventario
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Número de série: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ") .upper()
#Esta contrabarra \"S\" significa imprimir as aspas individualmente destacadas ali.


for elemento in inventario:
    print(elemento)
