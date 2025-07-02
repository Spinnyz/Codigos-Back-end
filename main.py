opções = (f"""
[D]- Deposito
[S]- Saque
[E]- Extrato
[Q]- Sair
""")


saque = 0
deposito = 0
limite = 500
saldo = 0
extrato = ""
LIMITE_SAQUE = 3



while True:
    print (opções)
    escolha = input(f"Digite a opção desejada:").upper().strip()

    #Deposito
    if escolha == "D":
        dep = float(input("Qual o valor de deposito:")) 
        #Negativo
        if dep <= 0:
             print("Valor invalido tente novamente")
             continue
    
    #deposito correto
        else: 
            saldo+=dep
            print(f" Seu novo saldoX é {saldo:.2f}")
            #extrato
            extrato += f"Deposito no valor de  R${dep}"

    #saque
    elif escolha == "S":
        saq = float(input("Digite o valor de Saque:"))
        if saq > saldo:
            print("Valor insificiente")
            continue
        elif saq <= 0:
            print ("O valor minimo é R$1")
        