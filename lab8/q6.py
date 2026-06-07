while True:
    valor = int(input('Digite o valor que deseja sacar: R$ '))

    if valor % 10 != 0:
        print("Não é possível sacar esse valor")
        continue

    if valor < 20:
        print("Não é possível sacar esse valor")
        continue

    if valor == 30:
        print("Não é possível sacar esse valor")
        continue

    print("Saque realizado com sucesso")
    break
