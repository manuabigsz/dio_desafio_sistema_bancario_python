class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    numero_conta = 0
    agencia = "0001"

    def __init__(self, usuario):
        ContaCorrente.numero_conta += 1
        self.numero = ContaCorrente.numero_conta
        self.usuario = usuario
        self.saldo = 0.0
        self.limite = 500
        self.limite_diario = 3
        self.saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")

    def sacar(self, valor):
        if self.saques < self.limite_diario:
            if valor > self.limite:
                print("Falha! Valor de saque excedido")
            elif valor > self.saldo:
                print("Falha! Saldo insuficiente")
            elif valor > 0:
                self.saldo -= valor
                self.extrato.append(f"Saque: R$ {valor:.2f}")
                self.saques += 1
            else:
                print("Valor inválido de saque")

    def exibir_extrato(self):
        if not self.extrato:
            print("Nenhuma operação foi realizada.")
        else:
            for operacao in self.extrato:
                print(operacao)
            print(f"\nSaldo: R$ {self.saldo:.2f}")

def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (logradouro, número - bairro - cidade/estado): ")
    cpf_numeros = ''.join(filter(str.isdigit, cpf))  # Extrai apenas os dígitos do CPF
    if any(u.cpf == cpf_numeros for u in usuarios):
        print("CPF já cadastrado!")
        return None
    return Usuario(nome, data_nascimento, cpf_numeros, endereco)

def cadastrar_conta(usuarios, contas):
    usuario = None
    while not usuario:
        cpf = input("Digite o CPF do usuário para associar a conta: ")
        cpf_numeros = ''.join(filter(str.isdigit, cpf))
        usuario = next((u for u in usuarios if u.cpf == cpf_numeros), None)
        if not usuario:
            print("Usuário não encontrado!")

    conta = ContaCorrente(usuario)
    contas.append(conta)
    print(f"Conta criada com sucesso para o usuário {usuario.nome}!")
    return conta

def listar_usuarios(usuarios):
    if not usuarios:
        print("Não há usuários cadastrados.")
    else:
        print("Lista de Usuários:")
        for idx, usuario in enumerate(usuarios, start=1):
            print(f"{idx}. Nome: {usuario.nome} | CPF: {usuario.cpf} | Endereço: {usuario.endereco}")

def realizar_deposito(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    numero_conta = int(input("Digite o número da conta para realizar o depósito: "))
    conta = next((c for c in contas if c.numero == numero_conta), None)
    if conta:
        valor_deposito = float(input('Informe o valor de depósito: '))
        conta.depositar(valor_deposito)
        print("Depósito realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def realizar_saque(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    numero_conta = int(input("Digite o número da conta para realizar o saque: "))
    conta = next((c for c in contas if c.numero == numero_conta), None)
    if conta:
        valor_saque = float(input("Informe o valor a ser sacado: "))
        conta.sacar(valor_saque)
    else:
        print("Conta não encontrada.")

def exibir_extrato(contas):
    if not contas:
        print("Não há contas cadastradas.")
        return

    numero_conta = int(input("Digite o número da conta para exibir o extrato: "))
    conta = next((c for c in contas if c.numero == numero_conta), None)
    if conta:
        conta.exibir_extrato()
    else:
        print("Conta não encontrada.")

def menu_principal():
    usuarios = []
    contas = []

    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1 - Criar usuário")
        print("2 - Criar conta")
        print("3 - Realizar depósito")
        print("4 - Realizar saque")
        print("5 - Exibir extrato")
        print("6 - Listar usuários")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_usuario = criar_usuario(usuarios)
            if novo_usuario:
                usuarios.append(novo_usuario)
        elif opcao == "2":
            if usuarios:
                cadastrar_conta(usuarios, contas)
            else:
                print("Não há usuários cadastrados!")
        elif opcao == "3":
            realizar_deposito(contas)
        elif opcao == "4":
            realizar_saque(contas)
        elif opcao == "5":
            exibir_extrato(contas)
        elif opcao == "6":
            listar_usuarios(usuarios)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()
