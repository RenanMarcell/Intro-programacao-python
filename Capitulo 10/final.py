import sys
import pickle
from functools import total_ordering
from listagem_10_13 import ListaUnica
from nome import Nome
from tipotelefone import TipoTelefone
from telefone import Telefone
from agenda import TiposTelefone, Agenda, DadoAgenda, Telefones


def nulo_ou_vazio(texto):
    return texto is None or not texto.strip()


def valida_faixa_inteiro(pergunta, inicio, fim, padrao=None):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada) and padrao is not None:
                entrada = padrao
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print('Valor invalido, favor digitar entre {} e {}'.format(inicio, fim))


def valida_faixa_inteiro_ou_branco(pergunta, inicio, fim):
    while True:
        try:
            entrada = input(pergunta)
            if nulo_ou_vazio(entrada):
                return None
            valor = int(entrada)
            if inicio <= valor <= fim:
                return valor

        except ValueError:
            print('Valor invalido, favor digitar entre {} e {}'.format(inicio, fim))


class Menu:
    def __init__(self):
        self.opcoes = [["Sair", None]]

    def adiciona_opcao(self, nome, funcao):
        self.opcoes.append([nome, funcao])

    def exibe(self):
        print("====")
        print("Menu")
        print("====\n")
        for i, opcao in enumerate(self.opcoes):
            print("[{0}] - {1}".format(i, opcao[0]))
        print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro(
                "Escolha uma opção: ",
                0,
                len(self.opcoes)
            )

            if escolha == 0:
                break
            self.opcoes[escolha][1]()


class AppAgenda:
    @staticmethod
    def pede_nome():
        return input("Nome: ")

    @staticmethod
    def pede_telefone():
        return input("Telefone: ")

    @staticmethod
    def mostra_dados(dados):
        print("Nome: {}".format(dados.nome))
        for telefone in dados.telefone:
            print("Telefone: {}".format(telefone))
        print()

    @staticmethod
    def mostra_dados_telefone(dados):
        print("Nome: {}".format(dados.nome))
        for i, telefone in enumerate(dados.telefone):
            print("{0} - Telefone: {1}".format(i, telefone))
        print()

    @staticmethod
    def pede_nome_arquivo():
        return input("Nome do arquivo: ")

    def __init__(self):
        self.agenda = Agenda()
        self.agenda.adiciona_tipo("Celular")
        self.agenda.adiciona_tipo("Residencia")
        self.agenda.adiciona_tipo("Trabalho")
        self.agenda.adiciona_tipo("Fax")
        self.menu = Menu()
        self.menu.adiciona_opcao("Novo", self.novo)
        self.menu.adiciona_opcao("Altera", self.altera)
        self.menu.adiciona_opcao("Apaga", self.apaga)
        self.menu.adiciona_opcao("Lista", self.lista)
        self.menu.adiciona_opcao("Grava", self.grava)
        self.menu.adiciona_opcao("Le", self.le)
        self.menu.adiciona_opcao("Ordena", self.ordena)
        self.ultimo_nome = None

    def pede_tipo_telefone(self, padrao=None):
        for i, tipo in enumerate(self.agenda.tipos_telefone):
            print(" {0} - {1} ".format(i, tipo), end=None)
        t = valida_faixa_inteiro("Tipo: ", 0,  len(self.agenda.tipos_telefone) - 1, padrao)
        return self.agenda.tipos_telefone[t]

    def pesquisa(self, nome):
        dado = self.agenda.pesquisa_nome(nome)
        return dado

    def novo(self):
        novo = AppAgenda.pede_nome()
        if nulo_ou_vazio(novo):
            return
        nome = Nome(novo)
        if self.pesquisa(nome) is not None:
            print("Nome já existe!")
            return
        registro = DadoAgenda(nome)
        self.menu_telefones(registro)
        self.agenda.adiciona(registro)

    def apaga(self):
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a apagar")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            self.agenda.remove(p)
            print("Apagado. A agenda agora possui apenas: {} registros".format(len(self.agenda)))
        else:
            print('Nome não encontrado')

    def altera(self):
        if len(self.agenda) == 0:
            print("Agenda vazia, nada a alterar")
        nome = AppAgenda.pede_nome()
        if nulo_ou_vazio(nome):
            return
        p = self.pesquisa(nome)
        if p is not None:
            print("\nEncontrado: \n")
            AppAgenda.mostra_dados(p)
            print("Digite enter caso não queira alterar o nome")
            novo = AppAgenda.pede_nome()
            if not nulo_ou_vazio(novo):
                p.nome = Nome(novo)
            self.menu_telefones(p)
        else:
            print("Nome não encontrado")

    def menu_telefones(self, dados):
        while True:
            print("\nEditando telefones\n")
            AppAgenda.mostra_dados_telefone(dados)
            if len(dados.telefones) > 0:
                print("\n[A] - alterar\n[D] - Apagar\n", end="")
            print("[N] - novo\n[S] - Sair\n")
            operacao = input("Escolha uma operação")
            operacao = operacao.lower()
            if operacao not in ['a', 'd', 'n', 's']:
                print("Operação inválida, digite A, D, N ou S")
                continue
            if operacao == 'a' and len(dados.telefones) > 0:
                self.altera_telefones(dados)
            elif operacao == 'd' and len(dados.telefones) > 0:
                self.apaga_telefone(dados)
            elif operacao == 'n':
                self.novo_telefone(dados)
            elif operacao == 's':
                break

    def novo_telefone(self, dados):
        telefone = AppAgenda.pede_telefone()
        if nulo_ou_vazio(telefone):
            return
        if dados.pesquisa_telefone(telefone) is not None:
            print("Telefone já existe")
        tipo = self.pede_tipo_telefone()
        dados.telefones.adiciona(Telefone(telefone, tipo))

    def apaga_telefone(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do numero a apagar, enter para sair:",
            0,
            len(dados.telefone - 1)
        )
        if t is None:
            return
        dados.telefone.remove(dados.telefones[t])

    def altera_telefones(self, dados):
        t = valida_faixa_inteiro_ou_branco(
            "Digite a posição do numero a alterar, enter para sair:",
            0,
            len(dados.telefone - 1)
        )
        if t is None:
            return
        telefone = dados.telefones[t]
        print("Telefone: %s" % telefone)
        print("Digite enter caso não queira alterar o número")
        novotelefone = AppAgenda.pede_telefone()
        if not nulo_ou_vazio(novotelefone):
            telefone.numero = novotelefone
        print("Digite enter caso não queira alterar o tipo")
        telefone.tipo = self.pede_tipo_telefone(
            self.agenda.tipos_telefone.pesquisa(telefone.tipo)
        )

    def lista(self):
        print("\nAgenda")
        print("-"*60)
        for e in self.agenda:
            AppAgenda.mostra_dados(e)
        print("-"*60)

    def le(self, nome_arquivo=None):
        if nome_arquivo is None:
            nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            return
        with open(nome_arquivo, 'rb') as arquivo:
            self.agenda = pickle.load(arquivo)
        self.ultimo_nome = nome_arquivo

    def ordena(self):
        self.agenda.ordena()
        print("\nAgenda ordenada")

    def grava(self):
        if self.ultimo_nome is not None:
            print("Ultimo nome ultilizado foi '%s'" % self.ultimo_nome)
            print("Digite enter caso queira utilizar o mesmo nome")
        nome_arquivo = AppAgenda.pede_nome_arquivo()
        if nulo_ou_vazio(nome_arquivo):
            if self.ultimo_nome is not None:
                nome_arquivo = self.ultimo_nome
            else:
                return

        with open(nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.agenda, arquivo)

    def execute(self):
        self.menu.execute()


if __name__ == "__main__":
    app = AppAgenda()
    if len(sys.argv) > 1:
        app.le(sys.argv[1])
    app.execute()
