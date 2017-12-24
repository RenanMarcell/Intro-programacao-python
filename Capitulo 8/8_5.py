def pesquise(L, valor):
    try:
        return 'Valor encontrado no índice {}'.format(L.index(valor))
    except ValueError:
        return 'Valor não encontrado'


if __name__ == "__main__":
    lista = []
    opt = input("Digite os valores da lista[fim para parar]: ").lower()
    while True:
        if opt == 'fim':
            break
        lista.append(opt)
        opt = input("Digite os valores da lista[fim para parar]: ").lower()

    search = input("Digite o valor a ser procurado na lista: ")
    print(pesquise(lista, search))
