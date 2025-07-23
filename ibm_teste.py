def menu():
    menu = """
    ========== MENU ==========
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    => """
    return input(menu)

# ---------- FUNÇÕES BANCÁRIAS ----------

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
    elif valor > limite:
        print("Valor acima do limite.")
    elif num_saques >= limite_saques:
        print("Limite de saques diários atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
    else:
        print("Valor inválido.")
    return saldo, extrato, num_saques

def mostrar_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Nenhuma movimentação.")
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")

# ---------- USUÁRIOS E CONTAS ----------

def criar_usuario(usuarios):
    cpf = input("CPF (somente números): ")
    if filtrar_usuario(cpf, usuarios):
        print("Usuário já existe.")
        return

    nome = input("Nome completo: ")
    nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta(agencia, numero_conta, usuarios, contas):
    cpf = input("CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        contas.append({"agencia": agencia, "numero": numero_conta, "usuario": usuario})
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"\nAgência: {conta['agencia']}")
        print(f"Conta: {conta['numero']}")
        print(f"Titular: {conta['usuario']['nome']}")

# ---------- EXECUÇÃO PRINCIPAL ----------

def main():
    saldo = 0
    extrato = ""
    limite = 500
    num_saques = 0
    LIMITE_SAQUES = 3

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato, num_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                num_saques=num_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta("0001", numero_conta, usuarios, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
