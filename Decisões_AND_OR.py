nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca = input("Suspeita de doença infecto-contagiosa? ").upper()
if idade >= 65 and doenca == "SIM":
    print("O paciente será direcionado para sala reservada -COM prioridade")
elif idade < 65 and doenca == "SIM":
    print("O paciente será direcionado para sala reservada -SEM prioridade")
elif idade >= 65 and doenca != "SIM":
    print("O paciente será direcionado para sala comum -COM prioridade")
else:
    print("O paciente será direcionado para sala comum -SEM prioridade")