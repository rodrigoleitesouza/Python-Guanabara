print("---------------------------------------------------")

phrase = str(input("Digite uma frase: ")).strip().upper()

words = phrase.split()

joinedWords = "".join(words)

upsidedown = ""

print("---------------------------------------------------")

for letter in range((len(joinedWords) - 1), -1, -1):
    upsidedown += joinedWords[letter]

print("O inverso de {0} é {1}.".format(phrase, upsidedown))

print("---------------------------------------------------")

if (upsidedown == joinedWords):
    print("Logo, a frase digitado é um palíndromo.")
else:
    print("Logo, a frase digitado não é um palíndromo.")

print("---------------------------------------------------")
print("Encerrando...")
print("---------------------------------------------------")
