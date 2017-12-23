if __name__ == "__main__":
    x = 0
    l1 = []
    l2 = []
    while x < 2:
        opt = int(input("Digite 1 para adicionar numeros na lista {}. 0 para avançar".format(x+1)))
        if opt == 0:
            x += 1
        elif opt == 1 and x == 0:
            l1.append(int(input("Digite o valor a ser adicionado: ")))
        elif opt == 1 and x == 1:
            l2.append(int(input("Digite o valor a ser adicionado: ")))
        else:
            print('Valor inválido')

    l3 = list()
    l3.append(l1)
    l3.append(l2)
    print(l3)
