# fazer um algoritmo para detectar quantos numeros positivos e negativos foram lidos
positivos = []
negativos = []

for c in range (1,6):
    valor = int(input('Digite algum número: '))
    if valor >= 0:
        positivos.append(valor)
    else:
        negativos.append(valor)

print(f'Foram digitados {len(positivos)} números positivos, sendo eles {positivos}')
print(f'Foram digitados {len(negativos)} números negativos, sendo eles {negativos}')
