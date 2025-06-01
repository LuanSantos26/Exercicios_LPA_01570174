print("Bem-vindo ao Banco Bananal !")

saldo = 1000.00

while True:
    print("\nEscolha uma opção:")
    print("1 - Saldo em conta")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")

    escolha = int(input("Digite o número da opção desejada: "))

    if escolha == 1:
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
    elif escolha == 2:
        saque = float(input("Digite o valor do saque: R$ "))
        if saque <= saldo:
            saldo -= saque
            print(f"Saque realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif escolha == 3:
        deposito = float(input("Digite o valor do depósito: R$ "))
        saldo += deposito
        print(f"Depósito realizado com sucesso! Seu novo saldo é: R$ {saldo:.2f}")
    elif escolha == 4:
        print("Obrigado por utilizar o Banco Bananal! Até a próxima.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")