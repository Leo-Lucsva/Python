# ler do usuário 8 números sendo apenas 0 e / ou 1

# fazer o calculo de cada digito para a conversão decimal

# retornar o valor decimal convertido para o usuário

def bin_decimal ():
    binario = str(input('Digite 8 numeros (apenas 0 ou 1):\n'))
    reversebinario = binario[::-1]
    resultado = 0

    count = 0

    for number in range (0,len(reversebinario)):
        print(int(reversebinario[number]))

        if (int(reversebinario[number]) == 0) or (int(reversebinario[number]) == 1):
            mult = int(reversebinario[number]) * 2 ** number
            resultado += mult
            count += 1
        else:
            break

    if count == len(reversebinario):
        print(f'O número em decimal do binário {binario} é: {resultado}')
    else:
        print('DIGITE APENAS 0 OU 1!')    

def decimal_bin ():
    decimal = int(input('Digite o decimal: '))
    resultado = ''
    print(decimal)
    count = 0

    while True:
        if decimal == 0 or decimal == 1:
            break
        sobra = decimal % 2
        print(sobra)
        decimal = decimal // 2
        count += 1
        resultado = resultado + str(sobra)
        print('esse é aqui ', decimal)
        print(decimal != 1)

    resultado += str(sobra)
    print(sobra, ' sobra')
    print(resultado[::-1])

opcao = int(input('''O que deseja converter?
{1} Para converter de decimal para binário
{2} Para converter de binário para decimal
'''))

if opcao == 1:
    decimal_bin()
else:
    bin_decimal()    