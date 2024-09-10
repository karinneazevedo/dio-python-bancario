menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"\nValor R$ {valor_deposito} depositado!\n"
            print(f"Valor de R$ {valor_deposito} depositado!")

        else:
            print("Valor inválido!")
            
        

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))
        if valor_saque > 0:

            if (numero_saques < LIMITE_SAQUES) & (valor_saque <= limite):
                            
                if valor_saque > saldo:
                    print("Saldo insuficiente!")
            
                else:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"\nValor R$ {valor_saque} sacado!\n"
                    print(f"Valor R$ {valor_saque} sacado!")

            else:
                print("Limite ou valor do saque excedido!")
        else:
            print("Valor inválido!")
    
    elif opcao == "e":
        if extrato == "":
            print("""
                  EXTRATO:

        Não foram realizadas movimentações
                  """)
        else:
            print(f"""
            EXTRATO:
            {extrato}

            SALDO:
            {saldo}      
            """)

    elif opcao == "q":
        break

    else:
        print("Operacao inválida, por favor selecione novamente a operação desejada")

