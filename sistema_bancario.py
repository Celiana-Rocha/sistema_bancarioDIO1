import os
limpar_terminal = os.system('cls')


print('BANCO'.center(40, '-'))

menu = 'informe o que deseja: \n [D] depositar | [S] sacar | [E] Extrato | [1] Sair \n ->: '

extrato = ''
saques = 3
saldo = 0
limites_saques = 0
contagem_de_depositos = 0

while True:
    opcao = input(menu)

    if opcao == 'd':
        limpar_terminal
        print('DEPÓSITO'.center(40, '-'))
        saldo += float(input('quanto deseja depositar? '))

        if saldo < 0:
            print("apenas valores positivos porfavor!!." )
            saldo = 0
        else:
            print('Ação bem sucedida! Consulte extrato para ver o depósito.')
            contagem_de_depositos += 1
            limpar_terminal
            continue

    #saque
    elif opcao == 's':
        limpar_terminal
        print('SAQUE'.center(40, '-'))
        valor_recebido = input('me informe o valor do saque \n ->: ')

        conversor_float = float(valor_recebido)

        if limites_saques == saques:
            print('seu limite de saques foi excedido!! profavor volte amanhã.')
            limpar_terminal
            continue   
        elif conversor_float >= 500:
            print('voce tem um limite de valor por saque de R$ 500 e esse valor foi excedido.')
            limpar_terminal
            continue    
        elif conversor_float > saldo:
            print('Seu saque foi negado devida a quantidade excedida do valor disponivel!')
        elif conversor_float < saldo:
            saldo = saldo - conversor_float
            print('saque autorizado e feito com sucesso!')
            limites_saques += 1  
            limpar_terminal 
            continue



    
    #extrato
    elif opcao == 'e':
        print('EXTRATO'.center(40, '-'))
        print(
            f'''
                    seu extrato

depósitos feitos:{contagem_de_depositos}
saques feitos: {limites_saques}
seus saques disponiveis: {limites_saques}
saldo: R${saldo:.2f}

            '''
        )
        continue
    
    #sair
    else:
        print('SAINDO...'.center(40, '-'))
        limpar_terminal
        break

print('OBRIGADO POR UTILIZAR NOSSO SERVIÇO'.center(40, '-'))
