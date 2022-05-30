from random import randint
from time import sleep

print("-------------------------------------------------------------------------")

print('''Escolha abaixo o número correspondente à sua jogada:
-------------------------------------------------------------------------
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

print("-------------------------------------------------------------------------")

humanPlay = int(input("Escolha sua jogada: "))
computerPlay = randint (0,2)

if (humanPlay == 0):
    playNameHuman = "PEDRA"
if (humanPlay == 1):
    playNameHuman = "PAPEL"
if (humanPlay == 2):
    playNameHuman = "TESOURA"

if (computerPlay == 0):
    playNameComputer = "PEDRA"
if (computerPlay == 1):
    playNameComputer = "PAPEL"
if (computerPlay == 2):
    playNameComputer = "TESOURA"    

print("-------------------------------------------------------------------------")

print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)

print("-------------------------------------------------------------------------")
print("Sua jogada é {0}.".format(playNameHuman))
print("A jogada do computador é {0}.".format(playNameComputer))
print("-------------------------------------------------------------------------")

if computerPlay == 0: # COMPUTADOR ESCOLHEU PEDRA
    if humanPlay == 0:
        print("Resultado: -> EMPATE")
    elif humanPlay == 1:
        print("Resultado: -> Você VENCEU!")
    elif humanPlay == 2:
        print("Resultado: -> Você PERDEU!")
    else:
        print("Jogada inválida!")

elif computerPlay == 1: # COMPUTADOR ESCOLHEU PAPEL
    if humanPlay == 0:
        print("Resultado: -> Você PERDEU!")
    elif humanPlay == 1:
        print("Resultado: -> EMPATE")
    elif humanPlay == 2:
        print("Resultado: -> Você VENCEU!")
    else:
        print("Jogada inválida!")

elif computerPlay == 2: # COMPUTADOR ESCOLHEU TESOURA
    if humanPlay == 0:
        print("Resultado: -> Você VENCEU!")
    elif humanPlay == 1:
        print("Resultado: -> Você PERDEU!")
    elif humanPlay == 2:
        print("Resultado: -> EMPATE")
    else:
        print("Jogada inválida!")

print("-------------------------------------------------------------------------")
print("Encerrando...")
print("-------------------------------------------------------------------------")
