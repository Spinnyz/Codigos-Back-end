#Banco

#deposito
def depositar (saldo,valor,extrato):
    if valor > 0:
        saldo+= valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
    else:
        print('Operação falhou! O valor informado é inválido.')
    return saldo, extrato

#saque
def sacar(*, saldo, valor, extrato, limite=500, numero_saques=0, limite_saques=3):
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

