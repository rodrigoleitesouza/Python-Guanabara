import os

print("---------------------------------------------------")

exit = ""
count = 0

while (True):
    count = count + 1
    number = int(input("Qual valor deseja saber a tabuada? -> "))
    os.system('cls')
    print("---------------------------------------------------")
    if (number < 0):
        break
    for count in range(1, 10, +1):
        print("{0} x {1} = {2}".format(count, number, number*count))

    print("---------------------------------------------------")


print("Encerrando...")
print("---------------------------------------------------")
