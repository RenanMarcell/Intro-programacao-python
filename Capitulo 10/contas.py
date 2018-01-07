class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = list()

    def resumo(self):
        print("\nCC Nº {} Saldo: {}".format(self.numero, self.saldo))
        print("Proprietário(s) da conta: ")
        for cliente in self.clientes:
            print("Nome: {}".format(cliente.nome))
            print("Telefone: {}".format(cliente.telefone))

    def verificacao(self, valor):
        return True if self.saldo > valor > 0 else False

    def saque(self, valor):
        if self.verificacao(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("Saldo inferior ou valor inválido\n")
            return False

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(["DEPOSITO", valor])
        else:
            print("Deposito não pode ser de valor negativo\n")

    def extrato(self):
        print("Extrato CC Nº {}".format(self.numero))
        for o in self.operacoes:
            print('{} {}'.format(o[0], o[1]))
        print("Saldo: {} \n".format(self.saldo))
