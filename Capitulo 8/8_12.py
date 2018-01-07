def validacao(s, L):
    return True if s in L else False


if __name__ == '__main__':
    lista = []
    opt = input("Digite os valores da lista[fim para parar]: ").lower()
    while True:
        if opt == 'fim':
            break
        lista.append(opt)
        opt = input("Digite os valores da lista[fim para parar]: ").lower()
    c = input("Digite a string: ")
    print(validacao(c, lista))
