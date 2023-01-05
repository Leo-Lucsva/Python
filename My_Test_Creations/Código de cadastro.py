# código que salva as infos de login de um usuário
# Algo bem básico e provavelmente não seja a melhor forma de fazer, mas é um começo

from os.path import exists
from os import getcwd as getpath
from time import sleep

from os.path import exists
from os import getcwd as getpath
from time import sleep
from random import randint

print('-=' * 15)
print(f"{'BEM VINDO AO LLS BURGUER!!':^30}")
print('-=' * 15)
sleep(1)
print('Primeiro faça login para fazer seu pedido!')
sleep(1)


#VERIFICAR SE O CADASTRO EXISTE OU ESTÁ CERTO
def verificar_login (nome, senha, cadastro):
    dados_conta = open('dados_conta', 'r').read().split()
    for i in range(0, len(dados_conta), 2):
            dado_nome = dados_conta[i]
            dado_senha = dados_conta[i + 1]
       
            if dado_nome == nome:  
                if cadastro == True:
                    return False
                if dado_senha == senha:
                    return True    
                else: 
                    return False
    return False

#CRIAR CONTA
def criar_conta ():
    dados_conta = open('dados_conta', 'a')

    nome = str(input('Digite seu apelido sem espaços (Lembre-se dele): '))
    senha = str(input('Digite a senha: '))
    if verificar_login (nome, senha, True):
        dados_conta.write(f' {nome} {senha} ')
        dados_conta.close()

        sleep(1)
        dados_conta = open('dados_conta', 'r').read()
        print('CONTA REGISTRADA! AGORA FAÇA LOGIN!')
    else:
        sleep(0.5)
        print('-' * 15)
        print('APELIDO OU CONTA JÁ REGISTRADA!.... O QUE DESEJA FAZER? ')
        opcao = int(input('''
[1] Tentar criar conta novamente
[2] Fazer login
        '''))

        if opcao == 1:
            criar_conta()
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
            sleep(0.7)
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
    opcao_login = int(input('''Digite o que deseja:
[1] Para criar conta
[2] Para fazer login
    '''))

    match opcao_login:
        case 1:
            criar_conta()
        case 2:
            fazer_login()

inicio_login()

