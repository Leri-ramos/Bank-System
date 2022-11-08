class Banco:
    def __init__(self, digital, privado):
        self.agencias = [1000, 2000, 3000]
        self.clientes = list()
        self.contas = list()
        self._digital = digital
        self._privado = privado

    @property
    def Digital(self):
        return self._digital

    @Digital.setter
    def Digital(self, novo_digital):
        self._digital = novo_digital

    @property
    def Privado(self):
        return self._digital

    @Privado.setter
    def Privado(self, novo_privado):
        self._digital = novo_privado


    @property
    def imprimirPrivado(self):
        return self._privado





    def inserirCliente(self, cliente):
        self.clientes.append(cliente)

    def inserirConta(self, conta):
        self.contas.append(conta)

    def imprimir(self):
        print(f'Conta {self.contas} do cliente {self.clientes} aberta')
        print('Conta digital: ' )
