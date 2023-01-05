# ler do usuário 8 números sendo apenas 0 e / ou 1

# fazer o calculo de cada digito para a conversão decimal

# retornar o valor decimal convertido para o usuário

while True:

    def bin_decimal ():
        binario = str(input('Digite 8 numeros (apenas 0 ou 1):\n'))
        reversebinario = binario[::-1]
        resultado = 0

        count = 0

        for number in range (0,len(reversebinario)):

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

        return resultado  

    def decimal_bin ():
        decimal = int(input('Digite o decimal: '))
        resultado = ''
        print(decimal)
        count = 0

        while decimal != 0 and decimal != 1:
            sobra = decimal % 2
            decimal = decimal // 2
            count += 1
            resultado = resultado + str(sobra)
        
        resultado += str(decimal)
        resultado = resultado[::-1]
        return resultado

    opcao = int(input('''O que deseja converter?
    {1} Decimal para binário
    {2} Binário para decimal
    {3} Sair
    '''))

    if opcao == 1:
        resultado = decimal_bin()
    elif opcao == 2:
        resultado = bin_decimal()    
    else:
        break
    print(f'O resultado é igual a: {resultado}')  
