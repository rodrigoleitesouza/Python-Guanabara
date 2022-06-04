print("---------------------------------------------------")

tupleWords = (
    "camisa",
    "casaco",
    "casa",
    "jardim",
    "amor",
    "janela",
    "pedra",
    "mouse",
    "tabela",
    "controle",
    "garrafa",
)

for word in tupleWords:
    print(
        f"\nNa palavra {word.upper()} tem-se as seguintes vogais: -> ", end="")
    for letter in word:
        if letter.lower() in "aeiou":
            print(letter, end=" ")

print("")
print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
