import random

numero = random.randint(1, 10)
chances = 3

while chances > 0:
    num = int(input(f"Qual o número secreto? Você tem {chances} chances: "))

    if numero == num:
        print("Você acertou o número")
        break
    elif num < numero:
        print("maior")
    else:
        print("menor")

    chances -= 1

print(numero)
