def soma(L):
    total = 0
    for number in L:
        total += number

    return total


if __name__ == '__main__':
    lista = []
    opt = int(input("Digite os valores da lista[0 para parar]: "))
    while True:
        if opt == 0:
            break
        lista.append(opt)
        opt = int(input("Digite os valores da lista[0 para parar]: "))

    print('Valor da soma da lista: {}'.format(soma(lista)))
