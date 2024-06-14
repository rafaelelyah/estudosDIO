import textwrap
import re

def menu():
    menu = """\n
    ======= Bem Vindo(a) ao PyBank ========
    Por favor, digite a opção que deseja:\n
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tCadastrar nova conta
    [5]\tLista de contas cadastradas
    [6]\tCadastrar novo usuário
    [0]\tSair
    \n
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nVocê depositou R$ {}\n".format(valor)) 

    else:
        print("\nO valor digitado está incorreto, por favor, tente novamente.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, saques_realizados, limite_diario, valor_diario):
    saldo_insuficiente = valor > saldo
    limite_excedido = valor > limite
    limite_saques_excedido = saques_realizados >= limite_diario
    valor_diario_excedido = valor_diario >= limite

    if saldo_insuficiente:
        print("\nVocê não tem saldo suficiente para realizar esta operação.\n")

    elif limite_excedido:
        print("\nO valor solicitado é maior que o limite disponível para esta operação.\n")

    elif limite_saques_excedido:
        print("\nVocê excedeu a quantidade de saques disponíveis para esta conta.\n")

    elif valor_diario_excedido:
        print("\nVocê excedeu o limite de valor diário.\n")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        valor_diario += valor
        saques_realizados += 1
        print("\nVocê sacou R$ {}\n".format(valor)) 
        print(saques_realizados)
        print(valor_diario)

    else:
        print("A informação digitada é inválida, por favor, tente novamente.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n============ Extrato ============")
    print("Nenhuma movimentação realizada." if not extrato else extrato)
    print(f"Saldo\tR$ {saldo:.2f}")
    print("=================================")

def cadastrar_usuario(usuarios):
    cpf = input("\nInforme seu CPF (Apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    pattern = r"^\([0-9]{2}\) [9][0-9]{4}\-[0-9]{4}$"
    telefone = ""
    if usuario:
        print("\n Já existe um usuário cadastrado com este CPF!")
        return
    
    nome = input("\nInforme seu nome completo: ")
    data_nascimento = input("\nInforme sua data de nascimento (dd/mm/aaaa): ")
    print("""\n
          =======================================
          Agora, informe os dados do seu endereço:
          =======================================
          \n""")
    cep = input("\nInforme seu CEP: ")
    logradouro = input("\nInforme o nome da rua/avenida/travessa: ")
    
    while not re.match(pattern, telefone):
        validate = input("\nInforme seu número de telefone, com o seguinte formato: (XX) XXXXX-XXXX\n")
        if re.match(pattern, validate):
            telefone = validate
        else:
            print("\nPor favor, digite um número válido.")
            

    complemento = input("\nInforme o complemento (ex: Casa/Apartamento): ")
    bairro = input("\nInforme o bairro: ")
    cidade = input("\nInforme a cidade: ")
    estado = input("\nInforme o estado: ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "cep": cep, "logradouro": logradouro, "telefone": telefone, 
                     "complemento": complemento, "bairro": bairro, "cidade": cidade, "estado": estado})

    print("""\n
          ==============  ===============
          Usuário cadastrado com sucesso!
          ==============  ===============
          """)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] ==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = input("\nInforme seu CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta cadastrada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nNão há cadastro para este CPF, por favor, realize o cadastro e tente novamente!")

def listar_contas(contas):

    if len(contas) == 0:
        print("\nNão há contas cadastradas.")

    else: 
        for conta in contas:
            linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
            print("=" * 100)
            print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_DIARIO = 3
    saldo = 0
    extrato = ""
    limite = 500
    saques_realizados = 0
    valor_diario = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Informe quanto deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques_realizados=saques_realizados,
                limite_diario=LIMITE_DIARIO,
                valor_diario=valor_diario,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "6":
            cadastrar_usuario(usuarios)
        
        elif opcao == "0":
            break

        else:
            print("\nOpção inváilda, por favor, selecione uma opção dentre as disponíveis.\n")

main()