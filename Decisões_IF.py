nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infecto-contagiosa?").upper()
# O .upper() deixa a resposta em caixa alta para facilitar a comparação == que faremos a seguir.
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
elif doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " deve ser direcionado para sala de espera reservada.")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário e pode aguardar na sala comum!")
# Neste caso o else será executado apenas se as duas condições não forem atendidas.