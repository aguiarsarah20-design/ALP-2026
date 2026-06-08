maior = float('-inf')
soma = 0
while soma < 10: 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    soma += 1
print('O maior número é', maior)

