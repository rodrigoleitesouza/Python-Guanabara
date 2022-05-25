print("----------------------------------------------------------------------------------------------------------")
print("CARRO ALUGADO")
print("----------------------------------------------------------------------------------------------------------")

distance = float(input("Quantos KM você percorreu com o carro alugado? -> "))
days = float(input("Por quantos dias você alugou o carro? -> "))

distancePrice = (distance*0.15)
daysPrice = (days*60)
totalPrice = (distancePrice + daysPrice)

print("----------------------------------------------------------------------------------------------------------")

print("O preço total de aluguel do carro é R$ {0:.2f}.".format(totalPrice))

print("----------------------------------------------------------------------------------------------------------")
print("Encerrando...")
print("----------------------------------------------------------------------------------------------------------")
