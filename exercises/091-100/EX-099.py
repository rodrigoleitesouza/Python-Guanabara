def higherNumber(*numbers):
    biggestNumber = 0
    count = 0

    print("---------------------------------------------------")
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


# real code

higherNumber(5, 3, 8, 1)
higherNumber(6, 33, 88, 91)
higherNumber(53, 33, 18, 12)
higherNumber(75, 73, 18, 199)
higherNumber(57, 73, 81, 91)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
