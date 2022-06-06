print("---------------------------------------------------")

numberList = []

for count in range(0, 5, +1):
    number = (int(input("Digite um número: ")))

    if count == 0 or number > numberList[-1]:
        numberList.append(number)
    else:
        position = 0
        while position < len(numberList):
            if number <= numberList[position]:
                numberList.insert(position, number)
                break
            position = position + 1

print("---------------------------------------------------")

print(f"Sua lista é -> {numberList}")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
