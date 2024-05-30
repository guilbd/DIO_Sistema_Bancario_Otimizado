import textwrap

def menu():
    menu = """
    ============ MENU ============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Cadastrar nova conta
    [lc] Listar contas
    [nu] Novo usuário
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R$ {valor:.2f}\n'
    else:
        print("Valor inválido!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, qte_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = qte_saques >= limite_saques
    
    if excedeu_saldo:
        print("Saldo insuficiente!")
    elif excedeu_limite:
        print("Limite de saque excedido!")
    elif excedeu_saques:
        print("Limite de saques diários excedido!")
    else:
        saldo -= valor
        extrato += f'Saque de R$ {valor:.2f}\n'
        qte_saques += 1
        print("Saque realizado com sucesso!")
        
    return saldo, extrato, qte_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n==============EXTRATO==============")
    print("Não foram realizadas movimentações!" if not extrato else extrato)
    print(f"\nSaldo:\t\t R$ {saldo:.2f}\n")
    print("=======================================")
    
def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("Já existe cliente com esse CPF!")
        return
    
    nome = input("Digite o nome do cliente: ")
    dt_nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o endereço [logradouro, nº, bairro, cidade/estado]: ")
    
    clientes.append({"nome": nome, "data_nascimento": dt_nascimento, "cpf": cpf, "endereco": endereco})
    print("Cliente cadastrado com sucesso!")

def cadastrar_conta(agencia, numero_conta, clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("Conta cadastrada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("Cliente não encontrado!")
    return None

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | Cliente: {conta['cliente']['nome']}")

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        if opcao == 'd':
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                qte_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, clientes)
            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'nu':
            cadastrar_cliente(clientes)
        elif opcao == 'q':
            break
        else:
            print("Opção inválida!")

main()
