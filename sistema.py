saldo = 0.0
limite = 500
limite_diario = 3
saques = 0
extrato = ''

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

def sacar(valor):
    global saldo, extrato, saques
    if saques < limite_diario:
        if valor > limite:
            print("Falha! Valor de saque excedido")
        elif valor > saldo:
            print("Falha! Saldo insuficiente")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1
        else:
            print("Valor inválido de saque")

def exibir_extrato():
    global extrato, saldo
    print("Nenhuma operação foi realizada." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")

menu = """
1 - depositar
2 - sacar
3 - extrato
0 - sair
"""

while True:
    op = input(menu)

    if op == "1":
        valor_deposito = float(input('Informe o valor de depósito: '))
        depositar(valor_deposito)

    elif op == "2":
        valor_saque = float(input("Informe o valor a ser sacado: "))
        sacar(valor_saque)

    elif op == "3":
        exibir_extrato()

    elif op == "0":
        break
    else:
        print("Opção inválida!")
