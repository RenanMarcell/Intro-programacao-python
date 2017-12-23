if __name__ == "__main__":
    L = []
    while True:
        opt = int(input("Digite 1 para adicionar numeros na lista. 0 para avançar\n"))
        if opt == 1:
            L.append(int(input("Digite o valor a ser adicionado: ")))
        elif opt == 0:
            break
        else:
            print('Valor inválido')

    l3 = list()
    for value in L:
        try:
            l3.index(value)
        except ValueError:
            l3.append(value)
    print(l3)
