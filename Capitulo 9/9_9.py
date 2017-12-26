if __name__ == '__main__':
    arquivos = []
    while True:
        nome = input('Digite o nome dos arquivos a serem lidos[fim para parar]: ')
        if nome.lower() == 'fim':
            break
        else:
            arquivos.append(nome)

    if len(arquivos) > 0:
        encontrado = False
        for nomes in arquivos:
            try:
                arquivo = open('files/{}'.format(nomes), 'r')
                encontrado = True
                for linha in arquivo.readlines():
                    print(linha)
            except FileNotFoundError:
                print('Arquivo não encontrado')

        if encontrado:
            arquivo.close()
    else:
        print('Lista de nomes vazia')
