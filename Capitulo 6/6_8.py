if __name__ == "__main__":
    L = [15, 7, 27, 39]
    p = int(input("Digite o valor a procurar: \n"))
    x = 0
    while x < len(L):
        if L[x] == p:
            break
        x += 1

    if x < len(L):
        print("%d achado na posição %d" % (p, x))
    else:
        print("%d não encontrado" % p)
