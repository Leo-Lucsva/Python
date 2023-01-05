impares = 0

for c in range (1,11):
    valor = int(input(f'{c}º valor:'))
    if valor % 2 == 1:
        impares += 1

porcentagem = impares / 10 * 100

print(f'A porcentagem entre os números impares e o total digitado é {porcentagem}%')
