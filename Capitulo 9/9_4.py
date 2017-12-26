if __name__ == '__main__':
    nome1 = input('Digite o nome do primeiro arquivo: ')
    nome2 = input('Digite o nome do segundo arquivo: ')
    arquivo1 = open('files/{}'.format(nome1), 'r')
    arquivo2 = open('files/{}'.format(nome2), 'r')
    arquivo3 = open('files/soma_arquivos.txt', 'w')

    for linha in arquivo1.readlines():
        arquivo3.write('%s\n' % linha)

    for linha in arquivo2.readlines():
        arquivo3.write('%s\n' % linha)

    arquivo1.close()
    arquivo2.close()
    arquivo3.close()
