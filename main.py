menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''


saldo = 0
limite = 500
extrato = ''
numeros_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input('-'*30+menu+'-'*30)

    if opcao == 'd':
        print('-'*30)
        print('Deposito')
        deposito = int(input('Quantos deseja depositar? R$'))
        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito feito de R${deposito:.2f}\n'
            print('Saque efetuado com sucesso')
        else:
            print('O valor do deposito tem que ser maior do que R$0,00')

    elif opcao == 's':
        print('-' * 30)
        print('Sacar')

        saque = int(input('Quantos deseja sacar? R$'))
        if saque > 0 and saque <= saldo and saque <= 500 and numeros_saques < LIMITE_SAQUES:
            saldo -= saque
            numeros_saques += 1
            extrato += f'Saque feito de R${saque:.2f}\n'
            print('Saque realizado com sucesso')
        elif numeros_saques == LIMITE_SAQUES:
            print('Nao é possivel realizar mais de 3 saques no dia')
        elif saque > 500:
            print('O saque deve ser inferior a R$500,00')
        else:
            print('Não foi possivel realizar o saque')


    elif opcao == 'e':
        print('-' * 30)
        print('Extrato')
        if extrato == '':
            print('Não foram realizadas movimentações')
        else:
            print(extrato+'-'*30+f'\nSaldo disponivel R${saldo:.2f}')

    elif opcao == 'q':
        print('-' * 30)
        print('Sair')
        break

    else:
        print('opcao invalida')