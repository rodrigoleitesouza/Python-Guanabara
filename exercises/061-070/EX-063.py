print("-------------------------------------------------------------------")

number = int(
    input("Quantos termos da sequência de fibonacci deseja descobrir? -> "))

count = 1

spot1 = 1
spot2 = 1
spot3 = 0

print("-------------------------------------------------------------------")

print("{0}...".format(spot3))

while (count < number):
    spot1 = spot2
    spot2 = spot3
    spot3 = spot2+spot1
    print("{0}...".format(spot3))

    count = count + 1

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
