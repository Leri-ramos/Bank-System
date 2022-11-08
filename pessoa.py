from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade, cpf, cidade):
        self.__nome = nome
        self._idade = idade
        self.__cpf = cpf
        self.cidade = cidade

class Funcionario(Pessoa):
    def __init__(self, matricula, cargo, salario):
        self.__matricula = matricula
        self._cargo = cargo
        self._salario = salario

class Cliente(Pessoa):
    def __init__(self, profissao, renda):
        self.profissao = profissao
        self.renda = renda