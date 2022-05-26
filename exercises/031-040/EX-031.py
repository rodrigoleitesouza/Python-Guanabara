print("--------------------------")
print("------ CONDICIONAIS ------")
print("--------------------------")

km = float(input("Quantos km você viajou? "))

print("--------------------------")

if (km <= 200):
    totalPrice = (km * 0.50)
    print("Total a pagar: R$ {0:.2f}".format(totalPrice))
else:
    totalPrice = (km * 0.45)
    print("Total a pagar: R$ {0:.2f}".format(totalPrice))

print("--------------------------")
print("Encerrando...")
print("--------------------------")
