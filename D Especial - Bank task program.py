valortotal = 100

def inicio():

    print('-='*15)
    print('CAIXA ELETRÔNICO')
    print('-='*15) 
    print(f'\033[32mSeu saldo é de R$ {valortotal}\033[m\n')

    def menu():
        opt = 0

        while opt < 1 or opt > 3:

            opt = int(input(('''DIGITE UMA DAS OPÇÕES:
----------------------
{1} Para sacar
{2} Para depositar
{3} Para pagar boleto
-----------------------
            ''')).strip())

            if opt <1 or opt > 3:
                print(f'OPÇÃO INVÁLIDA! -> {opt} <- NÃO É UMA OPÇÃO')

        opcoes(opt)

    def opcoes(opt):
        global valortotal
        match opt:
            case 1:
                saque = float(input('Digite o valor que deseja sacar:').strip())
                
                if valortotal >= saque:
                    valortotal -= saque
                    print('Boleto feito com sucesso!')
                    
                else:
                    print('VALOR INSUFICIENTE')
                    dep = int(input('Deseja depositar? \n {1} Para sim \n {2} para não \n'))

                    if dep == 1:
                        opcoes(2)

            case 2:
                deposito = float(input('Digite o valor que deseja depositar:').strip())
                valortotal += deposito
                print('Depósito feito com sucesso!')

            case 3:
                boleto = float(input('Digite o valor do boleto:').strip())
                
                if valortotal >= boleto:
                    valortotal -= boleto
                    print('Boleto feito com sucesso!')
                else:
                    print('VALOR INSUFICIENTE')
                    dep = int(input('Deseja depositar? \n {1} Para sim \n {2} para não \n'))

                    if dep == 1:
                        opcoes(2)
                              
        inicio()
    menu()

inicio()    