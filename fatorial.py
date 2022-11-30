fatorial = int(input('Qual número deseja saber o fatorial? '))
resultado = fatorial

for c in range (fatorial, 0, -1):
    print(c)

    if c - 1 == 0:
        break
    resultado = resultado * (c - 1)
    print(resultado)

print(f'O resultado foi de: {resultado}')    