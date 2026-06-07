total = 0

# cantina

while True:
    print('1- Salgados: R$ 5,00')
    print('2- Refrigerante: R$ 6,00')
    print('3- Suco: R$ 4,00')
    print('4- Fechar conta')

    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        total += 5

    elif opcao == 2:
        total += 6

    elif opcao == 3:
        total += 4

    elif opcao == 4:
        print('Total a pagar:', total)
        break

    else:
        print('Opção inválida')
        continue
