if __name__ == '__main__':
    nome = input('Digite o nome do arquivo: ')
    opcao = input('Deseja escrever ou ler o arquivo: ')
    if opcao != 'r' and opcao != 'w':
        print("Digite uma opção válida [w/r]: ")
        opcao = input('Deseja escrever ou ler o arquivo: ')
    if opcao == 'r':
        arquivo = open('files/{}'.format(nome), 'r')
        for linha in arquivo.readlines():
            print(linha)
    else:
        arquivo = open('files/{}'.format(nome), 'w')
        for linha in range(1, 1001):
            arquivo.write('%d\n' % linha)

    arquivo.close()
