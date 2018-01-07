from functools import total_ordering


@total_ordering
class Nome:
    def __init__(self, nome):  #1
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return "<Classe {3} em 0x{0:x} Nome: {1} Chave: {2}>".format(
            id(self),
            self.__nome,
            self.__chave,
            type(self).__name__
        )  #2

    def __eq__(self, outro):
        print("__eq__ Chamado")
        return self.nome == outro.nome

    def __lt__(self, outro):
        print("__lt__ Chamado")
        return self.nome < outro.nome

    @property  #3
    def nome(self):
        return self.__nome  #4

    @nome.setter  #5
    def nome(self, valor):
        if valor is None or not valor.strip():
            raise ValueError("Nome não pode ser nulo ou em branco")
        self.__nome = valor
        self.__chave = Nome.cria_chave(valor)

    @staticmethod
    def cria_chave(nome):
        return nome.strip().lower()
