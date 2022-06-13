from time import sleep


def count(start, end, increment):
    if (increment < 0):
        increment = increment*(-1)

    if (increment == 0):
        increment = 1

    if (start < end):
        for start in range(start, end+1, +increment):
            print(f'{start}... ', end="", flush=True)
            sleep(0.3)
        print()

    if (start > end):
        for start in range(start, end-1, -increment):
            print(f'{start}... ', end="", flush=True)
            sleep(0.3)
        print()


print("---------------------------------------------------")

start = int(input("Início: "))
end = int(input("Fim: "))
increment = int(input("Incremento: "))

print("---------------------------------------------------")

count(1, 10, 1)

print("---------------------------------------------------")

count(10, 0, 2)

print("---------------------------------------------------")

count(start, end, increment)

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
