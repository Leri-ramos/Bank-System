from banco import Banco
from conta import ContaCorrente, ContaPoupanca

print('='*71)
print('='*28, 'SISTEMA BANCO', '='*28)
print('='*71)

print('\n** Cadastro Novo Cliente - 0 \n** Cadastro Conta Corrente - 1 \n** Cadastro Conta Poupaca - 2 \n** Cliente - 3 \n')
op = int(input('Digite uma opcao: '))

if op == 0:
    global banco
    banco = Banco()
    banco.inserirCliente(input('Novo Cliente: '))
    banco.inserirConta(input('Nova Conta: '))
    banco.imprimir()

elif op == 1:
    global conta1
    conta1 = ContaCorrente(input('Agencia: '), banco.contas[len.contas-1], float(input('Deposito: ')))
    conta1.imprimirSaldoCC()

elif op == 2:
    global poup1
    poup1 = ContaPoupanca(1000, 123456, 0, 200)
    poup1.imprimirSaldoCP()

elif op == 3:
    conta1.depositar(30)
    conta1.imprimirSaldoCC()

else:
    print('Opcao invalida!')