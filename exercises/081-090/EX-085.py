print("---------------------------------------------------")

numberList = []

evenList = []

oddList = []

for count in range(1, 8, +1):
    number = int(input(f"{count}ª número: "))

    if (number % 2 == 0):
        evenList.append(number)
    else:
        oddList.append(number)

numberList.append(evenList)
numberList.append(oddList)

numberList[0].sort()
numberList[1].sort()

print("---------------------------------------------------")

print(numberList)

print("---------------------------------------------------")

print(numberList[0])

print("---------------------------------------------------")

print(numberList[1])

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
