print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

speed = float(input("Em qual velocidade (km/h) o carro está se deslocando? "))

tax = (speed - 80)*7

print("--------------------------")

if (speed <= 80):
    print("Você não foi multado! :D")
else:
    print("Você foi multado! :(")
    print("Valor da multa: R$ {0:.2f}".format(tax))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
