def triangulo(base, altura):
    return (base * altura)/2


if __name__ == '__main__':
    a = int(input("Digite o valor da base do triangulo: "))
    b = int(input("Digite o valor do altura do triangulo: "))
    print('Área do triangulo: {}'.format(triangulo(a, b)))
