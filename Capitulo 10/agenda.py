from listagem_10_13 import ListaUnica
from nome import Nome
from telefone import Telefone
from tipotelefone import TipoTelefone


class Telefones(ListaUnica):
    def __init__(self):
        super().__init__(Telefone)


class DadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefones = Telefones()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if type(valor) is not Nome:
            raise TypeError("nome deve ser uma instância da classe Nome")
        self.__nome = valor

    def pesquisa_telefone(self, telefone):
        posicao = self.telefones.pesquisa(Telefone(telefone))
        if posicao != -1:
            return None
        else:
            return self.telefones[posicao]


class TiposTelefone(ListaUnica):
    def __init__(self):
        super().__init__(TipoTelefone)


class Agenda(ListaUnica):
    def __init__(self):
        super().__init__(DadoAgenda)
        self.tipos_telefone = TiposTelefone()

    def adiciona_tipo(self, tipo):
        self.tipos_telefone.adiciona(TipoTelefone(tipo))

    def pesquisa_nome(self, nome):
        if type(nome) == str:
            nome = Nome(nome)
            for dados in self.lista:
                if dados.nome == nome:
                    return dados
        else:
            return None

    def ordena(self):
        super().ordena(lambda dado: str(dado.nome))
