class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = list()

    def adicionar_cidade(self, c):
        self.cidades.append(c)


class Cidade:
    def __init__(self, nome, populacao=0):
        self.nome = nome
        self.populacao = populacao


if __name__ == '__main__':
    cidades = []
    estados = []

    for x in range(9):
        name = input("Digite o nome da cidade {}: ".format(x+1))
        try:
            pop = int(input("Digite a populacao da cidade {}: ".format(x+1)))
        except ValueError:
            print('Deve ser um número')
        while pop < 0:
            try:
                pop = int(input("Digite a populacao da cidade {}: ".format(x + 1)))
            except ValueError:
                print('Deve ser um número')

        cidade = Cidade(name, pop)
        cidades.append(cidade)

    for x in range(3):
        name = input("Digite o nome do estado {}: ".format(x+1))
        sigl = input("Digite a sigla do estado {}: ".format(x+1))

        estado = Estado(name, sigl)
        estados.append(estado)

    x = 0
    y = 3
    for est in estados:
        popl = 0
        print('Estado: {}'.format(est.nome))
        for cid in cidades[x:y]:
            est.adicionar_cidade(cid)
            popl += cid.populacao
            print('Cidade: {} - População: {}'.format(cid.nome, cid.populacao))

        print('População total do estado: {}\n'.format(popl))
        x += 3
        y += 3
