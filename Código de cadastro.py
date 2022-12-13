# código que salva as infos de login de um usuário
# Algo bem básico e provavelmente não seja a melhor forma de fazer, mas é um começo

from os.path import exists
from os import getcwd as getpath
from time import sleep

#VERIFICAR SE O CADASTRO EXISTE OU ESTÁ CERTO
def verificar_login (nome, senha, cadastro):
    dados_conta = open('dados_conta', 'r').read().split()
    for i in range(0, len(dados_conta), 2):
            dado_nome = dados_conta[i]
            dado_senha = dados_conta[i + 1]
       
            if dado_nome == nome:  
                if cadastro == True:
                    print('falsoooo')
                    return False
                if dado_senha == senha:
                    return True    
                else: 
                    return False

#CRIAR CONTA
def criar_conta ():
    dados_conta = open('dados_conta', 'a')

    nome = str(input('Digite seu apelido sem espaços (Lembre-se dele): '))
    senha = str(input('Digite a senha: '))
    if not verificar_login (nome, senha, True):
        dados_conta.write(f' {nome} {senha} ')
        dados_conta.close()

        sleep(1)
        dados_conta = open('dados_conta', 'r').read()
        print(dados_conta)
        print('CONTA REGISTRADA! AGORA FAÇA LOGIN!')
    else:
        print('APELIDO OU CONTA JÁ REGISTRADA!.... FAÇA LOGIN ABAIXO:')
        
        sleep(0.7)
    fazer_login()

#FAZER LOGIN
def fazer_login ():
    
    if not exists(f'{getpath()}\dados_conta'):
        
        print('VOCÊ NÃO TEM CONTA CADASTRADA! Crie sua conta logo abaixo: ')
        criar_conta()
    else:
        
        nome = str(input('Digite o seu apelido: '))
        senha = str(input('Digite sua senha: '))

        if verificar_login(nome, senha, False):
            print(f'CADASTRO EFETUADO COM SUCESSO! É bom te ver por aqui {nome}!')
        else:
            print('APELIDO OU SENHA INCORRETOS!')
            sleep(1)
            
            opcao_login = int(input('''O que deseja fazer?
[1] Para criar conta
[2] Para Tentar novamente'''))

            if opcao_login == 1:
                criar_conta()
            elif opcao_login == 2:
                fazer_login()
            else:
                print('VALOR INVÁLIDO DIGITADO!')

# O QUE O CLIENTE QUER FAZER
def inicio_login ():
    opcao_login = int(input('''Digite:
    [1] Para criar conta
    [2] Para fazer login
    '''))

    match opcao_login:
        case 1:
            criar_conta()
        case 2:
            fazer_login()

inicio_login()

