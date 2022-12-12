from time import sleep

conta = ''
senha = ''

a = int(input('''Digite:
[1] Para criar conta
[2] Para acessar conta
'''))

if a == 1:
    conta = str(input('Digite qual será seu apelido (Lembre-se dele): '))
    senha = str(input('Digite qual será sua senha: '))

    dados_conta = open('dados_conta', 'w')
    dados_senha = open('dados_senha', 'w')
    
    dados_conta.write(conta)
    dados_senha.write(senha)

    dados_conta.close()
    dados_senha.close()

    print('CONTA CRIADA COM SUCESSO!')

elif a == 2:
    dados_conta = open('dados_conta', 'r').read()
    dados_senha = open('dados_senha', 'r').read()
    
    conta = str(input('Digite seu apelido: '))
    senha = str(input('Digite sua senha: '))

    if (conta == dados_conta) and senha == dados_senha:
        print('DADOS CORRETOS! VOCÊ ENTROU!', 'Olá', conta)
    else:
        print('DADOS INVÁLIDOS, TENTE NOVAMENTE!')