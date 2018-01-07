if __name__ == '__main__':
    nome = input('Digite o nome do arquivo: ')
    l_min = int(input("Digite a primeira linha a ser lida: "))
    l_max = int(input("Digite a ultima linha a ser lida: "))
    arquivo = open('files/{}'.format(nome), 'r')
    for idx, linha in enumerate(arquivo.readlines()):
        if l_min <= idx <= l_max:
            print(linha)

    arquivo.close()
