cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')

# quando digitamos números pares o codigó roda normalmente 
# com numeros pares fica imprimindo que o número é impar ate digitar um n par