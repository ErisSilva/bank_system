#Python - Variáveis
menu ="\n&&&&&-EríBankSystem-&&&&\n\nOquê deseja fazer?\n1-Depósito\n2-Saque\n3-Extrato\n4-Sair\n\n"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Menu de opções
while True:
    print(menu)
    # Tratar letras !
    try:
        opcao = int(input("Informe a opção!: "))
    except ValueError:
        print("\n\nEntrada inválida! >Por favor, digite apenas números<!.")
        continue  # Volta para o início do loop

    if opcao == 1:  # Depósito
        print("-------Depósito-------!\nDigite o valor do Depósito: ")
        valor = float(input())
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito!")    

    elif opcao == 2:  # Saque
        print("------Saque!------\nDigite o valor do Saque: ")
        valor = float(input())

        # Verificar se pode ou não sacar
        passou_saldo = valor > saldo
        passou_limite = valor > limite
        passou_saques = numero_saques >= LIMITE_SAQUES

        if passou_saldo:
            print("\nValor insuficiente!!!")  
        elif passou_limite:
            print("\nValor muito alto para operação!")
        elif passou_saques:
            print("\nNúmero máximo de saques atingido!!!")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("\nSaque realizado com sucesso!")

    elif opcao == 3:  # Extrato
        print("\n==== Extrato ====\n")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("\n===========\n")

    elif opcao == 4:  # Sair
        print("\nObrigado por usar a EríBankSystem!\n\n")
        break  

    else:
        print("\nInforme uma opção válida!!!\n\n")

