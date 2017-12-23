if __name__ == "__main__":
    estoque = {
            'tomate': [1000, 2.30],
            'alface': [500, 0.45],
            'batata': [2001, 1.20],
            'feijão': [100, 1.50]
        }
    vendas = []
    while True:
        opt = input("Digite o produto a ser vendido: (fim para acabar)\n")
        opt = opt.lower()
        if opt == 'fim':
            break
        try:
            qtd = estoque[opt][0]
            opt2 = int(input("Digite a quantidade do produto a ser vendido: "))
            if opt2 > qtd:
                print('Estoque menor do que o necessário')
            else:
                vendas.append([opt, opt2])

        except KeyError:
            print("Produto não em estoque")

    total = 0
    print("Vendas:\n")
    for operacao in vendas:
        produto, quantidade = operacao
        preco = estoque[produto][1]
        custo = preco * quantidade
        print("%12s: %3d x %6.2f = %6.2f" % (produto, quantidade, preco, custo))
        estoque[produto][0] -= quantidade
        total += custo
    print("\nCusto total: %21.2f\n" % total)
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição:", chave)
        print("Quantidade:", dados[0])
        print("Preço:%6.2f" % dados[1])
