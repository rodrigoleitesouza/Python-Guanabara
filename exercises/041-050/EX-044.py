print("----------------------------------------------")
print("------ CONDICIONAIS ANINHADAS ----------------")
print("----------------------------------------------")

price = float(input("Qual o preço do produto desejado? -> R$ "))

print("---------------------------------------------------")

print("[1] À vista em dinheiro (10% de desconto)")
print("[2] À vista no cartão (5% de desconto)")
print("[3] 2x no cartão (preço normal)")
print("[4] 3x ou mais no cartão (20% de juros)")

print("---------------------------------------------------")

typeOfPayment = int(input("Escolha o número corresponde ao modo de pagamento desejado: -> "))

print("---------------------------------------------------")

if (typeOfPayment == 1):
    newPrice = (price * 0.90)
    print("O preço correspondente a forma de pagamento escolhida é R$ {0:.2f}".format(newPrice))
elif (typeOfPayment == 2):
    newPrice = (price * 0.95)
    print("O preço correspondente a forma de pagamento escolhida é R$ {0:.2f}".format(newPrice))
elif (typeOfPayment == 3):
    newPrice = price
    print("O preço correspondente a forma de pagamento escolhida é R$ {0:.2f}".format(newPrice))
elif (typeOfPayment == 4):
    newPrice = (price * 1.20)
    print("O preço correspondente a forma de pagamento escolhida é R$ {0:.2f}".format(newPrice))

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
