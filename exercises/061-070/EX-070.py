count = 0
sumPrice = 0
productsUpper1000 = 0
lowestPrice = 999**999
lowestPriceName = ""

while(True):
    exit = ""
    count = count + 1

    print("---------------------------------------------------")
    name = str(input(f"{count}º PRODUTO / NOME: "))
    price = float(input(f"{count}º PRODUTO / PREÇO: R$ "))

    sumPrice = sumPrice + price

    if (price > 1000):
        productsUpper1000 = productsUpper1000 + 1

    if (lowestPrice > price):
        lowestPrice = price
        lowestPriceName = name

    while (exit != "N" and exit != "S"):
        print("---------------------------------------------------")
        exit = str(input("Gostaria de continuar? [S/N] -> ")).upper()

    if (exit == "N"):
        break

print("---------------------------------------------------")
print(f"Total gasto -> {sumPrice}")
print("---------------------------------------------------")
print(f"Qtd de produtos acima de R$ 1000 -> {productsUpper1000}")
print("---------------------------------------------------")
print(f"Nome do produto mais barato -> {lowestPriceName}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
