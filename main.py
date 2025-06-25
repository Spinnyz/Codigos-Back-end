print("Bem-vindo ao Seara Bancus")

saldo = 1000

while True:
    escolha = input("\nO que você deseja fazer? \n 1 - Depositar \n 2 - Sacar \n 3 - Ver Saldo \n 4 - Sair \n")

    if escolha == "1":
        deposito = int(input("Quanto você deseja depositar? \n"))
        saldo += deposito
        print(f"Seu novo saldo é: {saldo}")

    elif escolha == "2":
        saque = int(input("Quanto você deseja sacar? \n"))
        if saque > saldo:
            print("Saldo insuficiente")
        else:
            saldo -= saque
            print(f"Seu novo saldo é: {saldo}")

    elif escolha == "3":
        print(f"Seu saldo é: {saldo}")

    elif escolha == "4":
        print("Obrigado por usar o Seara Bancus, volte sempre!")

    else:
        print("Opção inválida. Tente novamente!")
