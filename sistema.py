saldo = 0.0
limite = 500
limite_diario = 3
saques=0
extrato = ''


menu = """
1 - depositar
2 - sacar
3 - extrato
0 - sair
"""


while True:
    op = input(menu)

    if(op == "1"):
        dep = float(input('informe o valor de depósito: '))
        
        if(dep > 0):
            saldo += dep 
            extrato  += f"Depósito: R$ {dep:.2f}\n"
        

    elif (op == "2"):
        if(saques < limite_diario):
            saq = float(input("Informe o valor a ser sacado: "))
            if(saq > limite):
                print("Falha! Valor de saque excedido")
            elif(saq > saldo):
                print("Falha! Saldo insuficiente")
            elif saq > 0:
                saldo -= saq
                extrato += f"Saque: R$ {saq:.2f}\n"
                saques += 1
            else:
                print("Valor inválido de saque")


    elif(op=="3"):
            print("Nenhuma operação foi realizada." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")


    elif(op == "0"):
        break
    else:
        print("Opção inválida!")