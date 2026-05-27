import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite < 1 or palpite > 10:
        print('invalido')
        continue
    if palpite == secreto:
      print('correto')  
      break
  
    chances -= 1