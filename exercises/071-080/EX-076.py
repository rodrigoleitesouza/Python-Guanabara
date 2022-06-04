print("-" * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print("-" * 40)

count = 0

tupleNamesAndPrices = (
    "Pão",
    10,
    "Leite",
    5,
    "Ovos",
    10,
    "Salsicha",
    25,
    "Arroz",
    56,
    "Carne",
    34,
    "Chocolate",
    6,
    "Farinha",
    5,
    "Lasanha",
    12,
)

for count in range(0, len(tupleNamesAndPrices), +1):
    if (count % 2 == 0):
        print(
            f"{tupleNamesAndPrices[count]:.<30} R$ {tupleNamesAndPrices[count+1]:.2f}")


print("-" * 40)
print("Encerrando...")
print("-" * 40)
