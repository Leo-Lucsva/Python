# Criar um programa de i food, onde a a pessoa vai logar com senha e nome;
# vai escolher qual lanche vai querer e esse lanche será adicionado a um carrinho 
# adicionar opção para ver o carrinho
# quando ela selecionar tudo o que vai querer, o endereço caso for entrega (R$ 5 entrega) ou retirada
# e o valor total da compra, além da forma de pagamento

# O QUE O CLIENTE QUER FAZER

opcao_login = int(input('''Digite:
[1] Para criar conta
[2] Para fazer login
'''))

match opcao_login:
    case 1:
        criar_conta()
    case 2:
        fazer_login

#FAZER LOGIN

def fazer_login ():
    nome = str(input('Digite o seu apelido: '))
    senha = str(input('Digite sua senha: '))
    

#CRIAR CONTA
def criar_conta ():
    dados_conta = open('dados_conta', 'w')

    nome = str(input('Digite seu apelido (Lembre-se dele): '))
    senha = str(input('Digite a senha: '))

    dados_conta.write(f'{nome} {senha}')
    dados_conta.close()

    dados_conta = open('dados_conta', 'r').read()
    print(dados_conta)