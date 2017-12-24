def validacao(s, maximo, minimo):
    return True if minimo < len(s) < maximo else False


if __name__ == '__main__':
    a = int(input("Digite o tamanho maximo da string: "))
    b = int(input("Digite o tamanho minimo da string: "))
    c = input("Digite a string: ")
    print(validacao(c, a, b))
