from contas import Conta


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite

    def extrato(self):
        print("Extrato CC Nº {}".format(self.numero))
        for o in self.operacoes:
            print('{} {}'.format(o[0], o[1]))
        print("Saldo: {}".format(self.saldo))
        print("Limite: {}".format(self.limite))
        print("Total disponível para saque: {}\n".format(self.saldo + self.limite))

    def verificacao(self, valor):
        return True if self.saldo + self.limite > valor > 0 else False
