produtos = []

def controle ():
    while True:
        ato = int(input('''O que deseja fazer?
        [1] Para encontrar o valor dos itens
        [2] Para adicionar um novo valor
        [3] Ver a lista completa de itens
        '''))

        if ato == 1:
            encontrar = str(input('Qual item você deseja consultar o valor (digite o nome)? ').strip().upper())
            found = False

            for l in produtos:
                for c in l:
                    if encontrar == c:
                        print(f'Produto: {l[0]} Valor: {l[1]}')
                        found = True
                        break
            if found == False:
                print('VALOR NÃO ENCONTRADO..')

        elif ato == 2:
            adicionar()
        else:
            if len(produtos) == 0:
                print('NÃO HÁ NENHUM VALOR NA LISTA, ADICIONE-OS: ')
            else: 
                for l in produtos:
                    
                    print(f'Nome: {l[0]} ', end='')
                    print(f'Valor: {l[1]}')                    

def adicionar ():
    produto = 0
    valor = 0
    global produtos
    while True:
        produto = str(input('Digite o nome do produto que deseja adicionar:  (ESCREVA "SAIR" PARA CONTINUAR ').strip().upper())
        if produto == 'SAIR':
            controle()
            break
        valor = float(input('Digite o valor deste produto: '))

        produtos.append([produto,valor])

controle()