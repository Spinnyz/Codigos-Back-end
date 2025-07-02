opções = (f"""
[D] - Depósito
[S] - Saque
[E] - Extrato
[Q] - Sair
""")

saque = 0
deposito = 0
limite = 500
saldo = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    print(opções)
    escolha = input(f"Digite a opção desejada:").upper().strip()

    # Depósito
    if escolha == "D":
        dep = float(input("Qual o valor do depósito:")) 
        # Negativo
        if dep <= 0:
            print("Valor inválido, tente novamente")
            continue

        # Depósito correto
        else: 
            saldo += dep
            print(f"Seu novo saldo é R$ {saldo:.2f}")
            # Extrato

    # Saque
    elif escolha == "S":
        # Sem limite
        if LIMITE_SAQUE == 0:
            print("Você já fez as 3 transações do dia")
            continue
        else:
            saq = float(input("Digite o valor do saque:"))

        # Saque sem saldo
        if saq > saldo:
            print(f"Valor insuficiente para saque. Seu saldo atual é de R$ {saldo}")
            continue
        # Saque negativo
        elif saq <= 0:
            print("O valor mínimo é R$ 1")
            continue
        # Sem saldo
        elif saldo <= 0:
            print("Sem saldo para saque")
            continue
        # Saque autorizado
        else:
            saldo -= saq
            print(f"Seu novo saldo é R$ {saldo}")
            LIMITE_SAQUE -= 1
    #Extrato
    elif escolha == "E":
        print ("\n=========== EXTRATO ===========")
        print (f"\nSeu Saldo é de {saldo:.2f}")

    #Fim
    elif escolha == "Q":
        print("Volte sempre")
        break
        