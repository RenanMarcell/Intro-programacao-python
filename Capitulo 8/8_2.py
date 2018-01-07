def is_multiple(n1, n2):
    return '' if n1 % n2 == 0 else 'não '


if __name__ == '__main__':
    a = int(input("Digite o primeiro numero:"))
    b = int(input("Digite o segundo numero:"))
    print('{} {}é multiplo de {}'.format(a, is_multiple(a, b), b))
