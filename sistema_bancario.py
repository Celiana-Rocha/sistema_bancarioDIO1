import os
limpar_terminal = os.system('cls')


print('BANCO'.center(40, '-'))

def menu():
    menu = ''' 
    ============================== MENU ==============================
    informe o que deseja: \n
    [C] Cria user | [N] Nova conta | [L] Lista de contas | [D] Depositar | [S] Sacar | [E] Extrato | [1] Sair \n 
    ->: '''
    return input(menu)

def listar_contas(contas):
     for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n***** Usuário não encontrado, fluxo de criação de conta encerrado! *****")

limpar_terminal

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

limpar_terminal

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n***** Operação falhou! Você não tem saldo suficiente. *****")

    elif excedeu_limite:
        print("\n***** Operação falhou! O valor do saque excede o limite. *****")

    elif excedeu_saques:
        print("\n***** Operação falhou! Número máximo de saques excedido. *****")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

limpar_terminal

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n***** Já existe usuário com esse CPF! *****")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

limpar_terminal

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

limpar_terminal

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:R$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n***** Operação falhou! O valor informado é inválido. *****")

    return saldo, extrato

limpar_terminal

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        limpar_terminal
        opcao = menu()
        limpar_terminal

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            limpar_terminal

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
            limpar_terminal

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)
            limpar_terminal

        elif opcao == "c":
            criar_usuario(usuarios)
            limpar_terminal

        elif opcao == "n":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            limpar_terminal

        elif opcao == "l":
            listar_contas(contas)
            limpar_terminal

        elif opcao == "1":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

limpar_terminal
main()
