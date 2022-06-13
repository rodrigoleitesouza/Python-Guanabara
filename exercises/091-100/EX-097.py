def write(message):
    lenght = len(message) + 4
    print("-" * lenght)
    print(f'  {message}')
    print("-" * lenght)


print("---------------------------------------------------")

message = str(input("Digite sua mensagem aqui -> "))

write(message)

print("Encerrando...")
print("---------------------------------------------------")
