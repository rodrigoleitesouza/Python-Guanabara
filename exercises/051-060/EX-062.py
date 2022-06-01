print("---------------------------------------------------")

start = int(input("Qual será o primeiro termo da sua PA? -> "))

print("---------------------------------------------------")

index = int(input("Qual a razão da sua PA? -> "))

count = 1

increment = 1

print("---------------------------------------------------")

while (count < 11):
    print("{0}...".format(start))
    start = start + index
    count = count + 1

while (increment != 0):
    print("---------------------------------------------------")
    increment = int(input("Gostaria de mostrar mais quantos termos? -> "))
    print("---------------------------------------------------")
    newCount = count + increment

    if (increment != 0):
        while (count < newCount):
            print("{0}...".format(start))
            start = start + index
            count = count + 1

print("Encerrando...")
print("---------------------------------------------------")
