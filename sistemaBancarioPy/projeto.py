menu = """

======= Bem Vindo(a) ao SBPY (Sistema Bancário em Python) ========
Por favor, digite a opção que deseja:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
extrato = ""
saques_realizados = 0
limite_diario = 3
valor_diario = 0

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nVocê depositou R$ {}\n".format(valor)) 

        else:
            print("O valor digitado está incorreto, por favor, tente novamente.")
    
    elif opcao == "2":
        valor = float(input("Informe quanto deseja sacar: "))
        saldo_insuficiente = valor > saldo
        limite_excedido = valor > limite
        limite_saques_excedido = saques_realizados >= limite_diario
        valor_diario_excedido = valor_diario >= limite


        if saldo_insuficiente:
            print("\nVocê não tem saldo suficiente para realizar esta operação.\n")

        elif(limite_excedido):
            print("\nO valor solicitado é maior que o limite disponível para esta operação.\n")

        elif(limite_saques_excedido):
            print("\nVocê excedeu a quantidade de saques disponíveis para esta conta.\n")

        elif(valor_diario_excedido):
            print("\nVocê excedeu o limite de valor diário.\n")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques_realizados += 1
            valor_diario += valor
            print("\nVocê sacou R$ {}\n".format(valor)) 

        else:
            print("A informação digitada é inválida, por favor, tente novamente.")

    elif opcao == "3":
        print("\n============ Extrato ============")
        print("Nenhuma movimentação realizada." if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
        print("=================================")
    
    elif opcao == "0":
        break

    else:
        print("\nOpção inváilda, por favor, selecione uma opção dentre as disponíveis.\n")