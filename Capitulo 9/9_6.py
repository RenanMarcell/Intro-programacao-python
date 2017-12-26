if __name__ == '__main__':
    largura = 79
    entrada = open('files/entrada.txt', 'r')
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '=':
            print('{}{}'.format('=' * 40, linha))
        elif linha[0] == '.':
            input()
            print('{}'.format(linha))
        elif linha[0] == '>':
            print(linha[1:].rjust(largura))
        elif linha[0] == '*':
            print(linha[1:].center(largura))
        else:
            print(linha)

    entrada.close()
