from clientes import Cliente
from contas import Conta
from banco import Banco
from contaespecial import ContaEspecial


if __name__ == '__main__':
    joao = Cliente('João da Silva', '(11) 2732-2323')
    jose = Cliente('Jose Maria', '(21) 99382-2103')
    maria = Cliente('Maria Helena', '(51) 93823-1324')
    contaJM = Conta([joao, jose], '5532', 500)
    contaJ = Conta([maria], '2313')
    contaE = ContaEspecial([maria, joao], '1111', 1000, 300)
    tatu = Banco("Tatu")
    tatu.abre_conta(contaJM)
    tatu.abre_conta(contaJ)
    tatu.abre_conta(contaE)
    contaE.saque(1450)
    tatu.lista_contas()

