if __name__ == '__main__':
    nome = input('Digite o nome do arquivo: ')
    opcao = input('Deseja escrever ou ler o arquivo: ')
    if opcao != 'r' and opcao != 'w':
        print("Digite uma opção válida [w/r]: ")
        opcao = input('Deseja escrever ou ler o arquivo: ')
    if opcao == 'r':
        arquivo = open(nome, 'r')
        for linha in arquivo.readlines():
            print(linha)
    elif opcao == 'w':
        arquivo = open(nome, 'w')
        for linha in range(1, 11):
            arquivo.write('%d\n' % linha)

    arquivo.close()
