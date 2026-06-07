soma = 0
while True:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    if n < 0:
        continue
    soma = soma + n
    if soma > 100:
        break

print("Soma total:", soma)
