#Banco

#Criação de conta

contas = []  # lista, não dicionário

def criar_conta(contas):
    cpf = input("Digite seu CPF: ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido.")
        return
    
    if filtro_conta(cpf, contas):
        print("Usuário já existe.")
        return  
    
    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    endereco = input("Digite seu endereço: ")

    contas.append({"Nome": nome, "CPF": cpf, "Nascimento": nascimento, "Endereço": endereco})
    print("Registrado com sucesso!")
    
def filtro_conta(cpf, contas):
    for conta in contas:
        if conta["CPF"] == cpf:
            return contas
    return None



#deposito
def depositar (saldo,valor,extrato):
        if valor > 0:
            saldo+= valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido.')
        return saldo, extrato

#saque
def sacar(saldo, valor, extrato, limite=500, numero_saques=0, limite_saques=3):
    if saldo >= valor and valor > 0 and limite >= valor and numero_saques < limite_saques:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("ERRO")
    return saldo, extrato, numero_saques

#extrato
def exibir_extrato(*,saldo,extrato):
    print("\n===== EXTRATO =====")
    if extrato:
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("====================")


saldo = 0
extrato = ""
numero_saques = 0
limite = 500
limite_saques = 3

while True:
    print("""
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    """)
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques)
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato)
        
    elif opcao == "4":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


      x  