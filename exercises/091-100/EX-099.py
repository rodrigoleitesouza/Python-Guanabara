def higherNumber(*numbers):
    biggestNumber = 0
    count = 0

    print("Analisando os valores passados...")
    print("---------------------------------------------------")

    for count in range(0, len(numbers), +1):
        print(f"{numbers[count]}... ", end="")
    print()

    print("---------------------------------------------------")
    print(f"Total de números: {len(numbers)}")
    print("---------------------------------------------------")

    for count in range(0, len(numbers), +1):   
        if (numbers[count] > biggestNumber):
            biggestNumber = numbers[count]
        count = count + 1
    print(f'O maior número é {biggestNumber}.')

print("---------------------------------------------------")

higherNumber(5, 3, 8, 1)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
