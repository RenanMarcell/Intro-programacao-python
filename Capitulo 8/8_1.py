def maximo(n1, n2):
    return max(n1, n2)


if __name__ == '__main__':
    a = int(input("Digite o primeiro numero:"))
    b = int(input("Digite o segundo numero:"))
    print('O maior numero entre {} e {} é {}'.format(a, b, maximo(a, b)))
