print('-=' * 20)
print(f'{"BEM VINDO AO IFOOD DA ESQUINA":^40}')
print('-=' * 20)

# Criar um programa de i food, onde a a pessoa vai logar com senha e nome;
# vai escolher qual lanche vai querer e esse lanche será adicionado a um carrinho 
# adicionar opção para ver o carrinho
# quando ela selecionar tudo o que vai querer, o endereço caso for entrega (R$ 5 entrega) ou retirada
# e o valor total da compra, além da forma de pagamento

def fazer_login ():
    pass

def criar_login ():
    a = open('dados_conta', 'r').read()
    print(a)
    nome_conta = str(input('Digite seu apelido (Lembre-se dele): '))
    senha_conta = str(input('Digite sua senha: '))


print('Antes de fazer o seu pedido, faça login...')

opcao_logar = int(input('''Digite:
[1] Para criar conta
[2] Para acessar conta
'''))

if opcao_logar == 1:
    criar_login()

'''
if opcao_logar == 1:
    conta = str(input('Digite qual será seu apelido (Lembre-se dele): '))
    senha = str(input('Digite qual será sua senha: '))

    dados_conta = open('dados_conta', 'w')
    dados_senha = open('dados_senha', 'w')
    
    dados_conta.write(conta)
    dados_senha.write(senha)

    dados_conta.close()
    dados_senha.close()

    print('CONTA CRIADA COM SUCESSO!')

elif opcao_logar == 2:
    dados_conta = open('dados_conta', 'r').read()
    dados_senha = open('dados_senha', 'r').read()
    
    conta = str(input('Digite seu apelido: '))
    senha = str(input('Digite sua senha: '))

    if (conta == dados_conta) and senha == dados_senha:
        print('DADOS CORRETOS! VOCÊ ENTROU!', 'Olá', conta)
    else:
        print('DADOS INVÁLIDOS, TENTE NOVAMENTE!')
        '''