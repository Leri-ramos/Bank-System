from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def depositar(self, valor):
       pass

    @abstractmethod
    def sacar(self, valor):
        pass

    
class ContaCorrente(Conta):
    #Construtor da classe conta
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente!')

    def depositar(self, valor):
        self.saldo += valor 

    def imprimirSaldoCC(self):
        print(f'Saldo CC {self.saldo}.')
        

class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        # Construtor da classe conta 
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor  

    def sacar(self, valor):
        if (self.saldo + self.limite) >= valor:
            self.saldo -= valor

    def imprimirSaldoCP(self):
        print(f'Saldo CP {self.saldo}.')
        print(f'Limite {self.limite}.')
#class ContaSalario:


